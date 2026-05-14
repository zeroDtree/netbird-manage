#!/usr/bin/env python3
"""
NetBird user tools: bulk import (embedded IdP) or bulk delete by email.

Subcommands:
  import  — invite + accept from CSV/Excel (human users only).
  delete  — remove users by email (DELETE /api/users/{id}); requires --yes unless --dry-run.

import columns (case-insensitive):
  email, name, role, password, auto_groups (optional), expires_in (optional)

delete columns:
  email (required per row); other columns ignored

Environment: NETBIRD_API_BASE, NETBIRD_TOKEN (or --token).
Optional: a ``.env`` file in the current working directory is loaded automatically (same variable names).

Run: cd netbird && uv sync && uv run python user_manage.py import --file users.csv --dry-run
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
import time
from typing import Any

try:
    from dotenv import load_dotenv
    import requests

    from netbird_cli import netbird_connection_parent_parser
    from netbird_client import (
        api_url,
        json_headers,
        request_with_retry,
        response_status,
        session_with_token,
    )
    from netbird_groups import fetch_groups_map
    from netbird_users import (
        delete_user_by_id,
        email_to_user_id,
        existing_emails_from_users,
        fetch_users,
    )
    from netbird_validation import validate_email
except ImportError:
    print("Install dependencies: cd netbird && uv sync", file=sys.stderr)
    print(
        "Then: uv run python user_manage.py import|delete ...  (or: uv run netbird-user-manage ...)",
        file=sys.stderr,
    )
    raise


def _norm_header(h: str) -> str:
    return h.strip().lower().replace(" ", "_")


def _split_groups(cell: str | None) -> list[str]:
    if cell is None:
        return []
    s = str(cell).strip()
    if not s:
        return []
    if "|" in s:
        parts = [p.strip() for p in s.split("|")]
    else:
        parts = [p.strip() for p in s.split(",")]
    return [p for p in parts if p]


def validate_password_netbird(password: str) -> str | None:
    """Return error message if invalid, else None (embedded IdP accept rules)."""
    if len(password) < 8:
        return "password must be at least 8 characters"
    if not any(c.isupper() for c in password):
        return "password must contain at least one uppercase letter"
    if not any(c.isdigit() for c in password):
        return "password must contain at least one digit"
    if not any(not c.isalnum() for c in password):
        return "password must contain at least one special character (non-letter, non-digit)"
    return None


def load_rows_csv(path: str) -> list[dict[str, str]]:
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            raise ValueError("CSV has no header row")
        fieldmap = {_norm_header(h): h for h in reader.fieldnames}
        rows: list[dict[str, str]] = []
        for raw in reader:
            row: dict[str, str] = {}
            for key, orig in fieldmap.items():
                row[key] = (raw.get(orig) or "").strip()
            rows.append(row)
    return rows


def load_rows_xlsx(path: str) -> list[dict[str, str]]:
    try:
        import openpyxl
    except ImportError:
        raise RuntimeError(
            "Excel support requires: cd netbird && uv sync (includes openpyxl)"
        ) from None
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    ws = wb.active
    rows_iter = ws.iter_rows(values_only=True)
    try:
        header = next(rows_iter)
    except StopIteration:
        wb.close()
        raise ValueError("Excel sheet is empty")
    headers = [_norm_header(str(h) if h is not None else "") for h in header]
    if not any(headers):
        wb.close()
        raise ValueError("Excel has no header row")
    out: list[dict[str, str]] = []
    for tup in rows_iter:
        if tup is None or all(v is None or str(v).strip() == "" for v in tup):
            continue
        row: dict[str, str] = {}
        for i, key in enumerate(headers):
            if not key:
                continue
            val = tup[i] if i < len(tup) else None
            row[key] = "" if val is None else str(val).strip()
        if any(row.values()):
            out.append(row)
    wb.close()
    return out


def load_rows(path: str) -> list[dict[str, str]]:
    lower = path.lower()
    if lower.endswith(".csv"):
        return load_rows_csv(path)
    if lower.endswith(".xlsx") or lower.endswith(".xlsm"):
        return load_rows_xlsx(path)
    raise ValueError(f"unsupported file type: {path} (use .csv, .xlsx)")


def resolve_auto_groups(
    parts: list[str],
    *,
    resolve_names: bool,
    name_to_id: dict[str, str],
) -> tuple[list[str] | None, str | None]:
    if not parts:
        return [], None
    ids: list[str] = []
    for p in parts:
        if resolve_names:
            lid = name_to_id.get(p.lower())
            if lid:
                ids.append(lid)
            else:
                return None, f"unknown group name: {p!r}"
        else:
            ids.append(p)
    return ids, None


def invite_and_accept(
    session: requests.Session,
    base: str,
    email: str,
    name: str,
    role: str,
    auto_groups: list[str],
    password: str,
    expires_in: int | None,
) -> tuple[bool, str]:
    url_invite = api_url(base, "/api/users/invites")
    body: dict[str, Any] = {
        "email": email,
        "name": name,
        "role": role,
        "auto_groups": auto_groups,
    }
    if expires_in is not None:
        body["expires_in"] = int(expires_in)

    inv = request_with_retry(
        session,
        "POST",
        url_invite,
        headers=json_headers(),
        json_body=body,
    )
    if response_status(inv) >= 400:
        return False, f"invite failed: {response_status(inv)} {inv.text[:500]}"

    try:
        payload = inv.json()
    except json.JSONDecodeError:
        return False, "invite failed: invalid JSON response"

    token = payload.get("invite_token")
    if not token:
        return False, "invite failed: no invite_token in response"

    url_accept = f"{base.rstrip('/')}/api/users/invites/{token}/accept"
    acc = request_with_retry(
        session,
        "POST",
        url_accept,
        headers=json_headers(),
        json_body={"password": password},
    )
    if response_status(acc) >= 400:
        return False, f"accept failed: {response_status(acc)} {acc.text[:500]}"
    return True, "ok"


def append_error(path: str, record: dict[str, Any]) -> None:
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


def _parent_parser() -> argparse.ArgumentParser:
    p = netbird_connection_parent_parser()
    p.add_argument(
        "--delay-between-rows",
        type=float,
        default=0.35,
        metavar="SECONDS",
        help=(
            "Pause after each row's NetBird requests before continuing to the next row "
            "(rate limiting)."
        ),
    )
    return p


def run_import(args: argparse.Namespace) -> int:
    try:
        rows = load_rows(args.file)
    except Exception as e:
        print(f"Failed to read {args.file}: {e}", file=sys.stderr)
        return 2

    default_gids = _split_groups(args.default_auto_groups.replace(",", "|"))

    errors: list[tuple[int, str, str]] = []
    for i, row in enumerate(rows, start=2):
        email = row.get("email", "")
        name = row.get("name", "")
        role = row.get("role", "")
        pwd = row.get("password", "")
        line_ref = f"row {i} ({email or '?'})"

        if err := validate_email(email):
            errors.append((i, line_ref, err))
            continue
        if not name:
            errors.append((i, line_ref, "missing name"))
            continue
        if not role:
            errors.append((i, line_ref, "missing role"))
            continue
        if err := validate_password_netbird(pwd):
            errors.append((i, line_ref, err))

        parts = _split_groups(row.get("auto_groups"))
        eff = parts if parts else default_gids
        if not eff:
            errors.append(
                (i, line_ref, "auto_groups empty and no --default-auto-groups")
            )

    if errors:
        for _, line_ref, msg in errors:
            print(f"{line_ref}: {msg}", file=sys.stderr)
        return 3

    if args.dry_run:
        print(f"import dry run OK: {len(rows)} row(s) validated.")
        return 0

    if not args.token:
        print("Missing PAT: set NETBIRD_TOKEN or pass --token", file=sys.stderr)
        return 4

    session = session_with_token(args.token)

    users = fetch_users(session, args.base_url)
    existing = existing_emails_from_users(users)
    name_to_id: dict[str, str] = {}
    if args.resolve_group_names:
        name_to_id = fetch_groups_map(session, args.base_url)

    ok = 0
    skipped = 0
    failed = 0

    for i, row in enumerate(rows, start=2):
        email = row["email"].strip()
        name = row["name"].strip()
        role = row["role"].strip()
        pwd = row.get("password", "")
        expires_raw = row.get("expires_in", "").strip()
        expires_in = int(expires_raw) if expires_raw else None

        parts = _split_groups(row.get("auto_groups"))
        eff_parts = parts if parts else list(default_gids)
        ag, err = resolve_auto_groups(
            eff_parts, resolve_names=args.resolve_group_names, name_to_id=name_to_id
        )
        if err:
            failed += 1
            append_error(
                args.failure_log_jsonl,
                {"row": i, "email": email, "stage": "resolve_groups", "error": err},
            )
            print(f"row {i} {email}: {err}", file=sys.stderr)
            continue
        assert ag is not None

        el = email.lower()
        if el in existing:
            skipped += 1
            print(f"skip existing {email}")
            time.sleep(args.delay_between_rows)
            continue

        success, msg = invite_and_accept(
            session, args.base_url, email, name, role, ag, pwd, expires_in
        )
        if success:
            ok += 1
            existing.add(el)
            print(f"user {email} created (invite+accept)")
        else:
            failed += 1
            stage = "invite" if msg.startswith("invite") else "accept"
            append_error(
                args.failure_log_jsonl,
                {"row": i, "email": email, "stage": stage, "error": msg},
            )
            print(f"row {i} {email}: {msg}", file=sys.stderr)

        time.sleep(args.delay_between_rows)

    print(f"import done: ok={ok} skipped={skipped} failed={failed}")
    return 1 if failed else 0


def run_delete(args: argparse.Namespace) -> int:
    try:
        rows = load_rows(args.file)
    except Exception as e:
        print(f"Failed to read {args.file}: {e}", file=sys.stderr)
        return 2

    errors: list[tuple[int, str, str]] = []
    for i, row in enumerate(rows, start=2):
        email = row.get("email", "")
        line_ref = f"row {i} ({email or '?'})"
        if err := validate_email(email):
            errors.append((i, line_ref, err))

    if errors:
        for _, line_ref, msg in errors:
            print(f"{line_ref}: {msg}", file=sys.stderr)
        return 3

    if args.dry_run:
        print(f"delete dry run OK: {len(rows)} email row(s) validated.")
        return 0

    if not args.token:
        print("Missing PAT: set NETBIRD_TOKEN or pass --token", file=sys.stderr)
        return 4

    if not args.yes:
        print("Refusing to delete without --yes (or use --dry-run).", file=sys.stderr)
        return 5

    session = session_with_token(args.token)

    users = fetch_users(session, args.base_url)
    e2id = email_to_user_id(users)

    ok = 0
    skipped = 0
    failed = 0

    for i, row in enumerate(rows, start=2):
        email = row["email"].strip()
        el = email.lower()

        uid = e2id.get(el)
        if not uid:
            skipped += 1
            append_error(
                args.failure_log_jsonl,
                {
                    "row": i,
                    "email": email,
                    "stage": "resolve_user",
                    "error": "no user with this email",
                },
            )
            print(f"skip not_found {email}")
            time.sleep(args.delay_between_rows)
            continue

        r = delete_user_by_id(session, args.base_url, uid)
        del_code = response_status(r)
        if del_code == 404:
            skipped += 1
            print(f"skip already_deleted {email}")
            e2id.pop(el, None)
            time.sleep(args.delay_between_rows)
            continue
        if del_code < 400:
            ok += 1
            e2id.pop(el, None)
            print(f"deleted {email}")
            time.sleep(args.delay_between_rows)
            continue

        failed += 1
        msg = f"{del_code} {r.text[:500]}"
        append_error(
            args.failure_log_jsonl,
            {"row": i, "email": email, "stage": "delete", "error": msg},
        )
        print(f"row {i} {email}: {msg}", file=sys.stderr)
        time.sleep(args.delay_between_rows)

    print(f"delete done: ok={ok} skipped={skipped} failed={failed}")
    return 1 if failed else 0


def run(argv: list[str] | None = None) -> int:
    raw = list(sys.argv[1:] if argv is None else argv)
    # Populate os.environ from .env before argparse defaults read NETBIRD_*.
    load_dotenv()

    parent = _parent_parser()
    main = argparse.ArgumentParser(
        description="NetBird bulk user import (embedded IdP) or delete by email.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = main.add_subparsers(dest="command", required=True)

    p_imp = sub.add_parser(
        "import",
        help="Bulk invite + accept (create human users)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        parents=[parent],
        epilog="""
Examples:
  %(prog)s import --file users.csv --dry-run
  %(prog)s import --file users.csv --token "$NETBIRD_TOKEN"

Smoke (curl): see NetBird docs for POST /api/users/invites and .../accept.
""",
    )
    p_imp.add_argument("--file", "-f", required=True, help="Path to .csv or .xlsx")
    p_imp.add_argument(
        "--default-auto-groups",
        default="",
        help="Comma-separated group IDs when row auto_groups is empty",
    )
    p_imp.add_argument(
        "--resolve-group-names",
        action="store_true",
        help="Treat auto_groups column as group names (GET /api/groups map)",
    )
    p_imp.add_argument(
        "--failure-log-jsonl",
        default="netbird_import_errors.jsonl",
        help="Append one JSON object per failed import row to this file (JSON Lines)",
    )

    p_del = sub.add_parser(
        "delete",
        help="Delete users by email (NetBird only; see API re IdP)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        parents=[parent],
        epilog="""
CSV/Excel needs an email column. Other columns are ignored.

Destructive: pass --yes to perform DELETE (not needed with --dry-run).
""",
    )
    p_del.add_argument(
        "--file", "-f", required=True, help="Path to .csv or .xlsx (email column)"
    )
    p_del.add_argument(
        "--yes",
        action="store_true",
        help="Required for real deletes (omit with --dry-run only)",
    )
    p_del.add_argument(
        "--failure-log-jsonl",
        default="netbird_delete_errors.jsonl",
        help="Append one JSON object per failed delete row to this file (JSON Lines)",
    )

    args = main.parse_args(raw)

    if args.command == "import":
        return run_import(args)
    if args.command == "delete":
        return run_delete(args)
    raise RuntimeError(f"unknown command: {args.command}")


def main() -> None:
    """Console entry point for ``uv run netbird-user-manage`` / pip install."""
    raise SystemExit(run())


if __name__ == "__main__":
    main()
