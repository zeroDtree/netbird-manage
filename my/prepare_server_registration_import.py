#!/usr/bin/env python3
"""
Convert server registration Excel to user-manage import CSV.

Reads data/服务器申请登记.xlsx (or --input), maps spreadsheet columns via YAML
(default: my/server_registration_columns.yaml, override with --mapping), and
appends suffix Aa@ to passwords that fail NetBird validation.

Each run:
  1. Writes latest full export from the xlsx.
  2. Fetches registered emails from NetBird (GET /api/users).
  3. Writes pre_server_registration_emails.csv (registered email snapshot).
  4. Writes *_delta.csv with rows whose email is not yet registered in NetBird.

Outputs:
  - data/server_registration_import.csv (latest full export)
  - data/server_registration_passwords.csv (latest password mapping)
  - data/pre_server_registration_emails.csv (NetBird registered emails)
  - data/server_registration_import_delta.csv (rows to import)
  - data/server_registration_passwords_delta.csv (rows to notify)

Requires NETBIRD_TOKEN in .env (or --token). Run from repo root:
  uv run python my/prepare_server_registration_import.py
  uv run python my/prepare_server_registration_import.py -m my/server_registration_columns.yaml
"""

from __future__ import annotations

import argparse
import csv
import sys
from dataclasses import dataclass
from pathlib import Path

import requests
import yaml
from dotenv import load_dotenv

from netbird_manage.cli.user_manage import _norm_header, load_rows, validate_password_netbird
from netbird_manage.utils.cli import netbird_connection_parent_parser
from netbird_manage.utils.client import session_with_token
from netbird_manage.utils.netbird_validation import validate_email
from netbird_manage.vendor_api.users import existing_emails_from_users, fetch_users

_SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_MAPPING = _SCRIPT_DIR / "server_registration_columns.yaml"

DEFAULT_INPUT = Path("data/服务器申请登记.xlsx")
DEFAULT_OUTPUT = Path("data/server_registration_import.csv")
DEFAULT_PASSWORD_REPORT = Path("data/server_registration_passwords.csv")
DEFAULT_PRE_EMAILS = Path("data/pre_server_registration_emails.csv")
DEFAULT_SUFFIX = "Aa@"
DEFAULT_AUTO_GROUPS = "client_group"
DEFAULT_ROLE = "user"

# Built-in column headers (same as server_registration_columns.yaml).
_DEFAULT_EMAIL_HEADER = "邮箱（用作netbird登录账号）"
_DEFAULT_NAME_HEADER = "申请人真实姓名"
_DEFAULT_PASSWORD_HEADER = "netbird初始登录密码"

IMPORT_FIELDNAMES = ["email", "name", "role", "password", "auto_groups"]
REPORT_FIELDNAMES = ["email", "name", "password_original", "password_for_netbird"]
REGISTERED_FIELDNAMES = ["email"]


@dataclass(frozen=True)
class ColumnMapping:
    email_key: str
    name_key: str
    password_key: str


def column_mapping_from_headers(email: str, name: str, password: str) -> ColumnMapping:
    return ColumnMapping(
        email_key=_norm_header(email),
        name_key=_norm_header(name),
        password_key=_norm_header(password),
    )


DEFAULT_COLUMN_MAPPING = column_mapping_from_headers(
    _DEFAULT_EMAIL_HEADER,
    _DEFAULT_NAME_HEADER,
    _DEFAULT_PASSWORD_HEADER,
)


def load_column_mapping(path: Path) -> ColumnMapping:
    """Load columns.email|name|password from a YAML file."""
    with path.open(encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if not isinstance(data, dict):
        raise ValueError(f"mapping file must be a YAML mapping: {path}")

    cols = data.get("columns")
    if not isinstance(cols, dict):
        raise ValueError(f"mapping file must define columns.email, columns.name, columns.password: {path}")

    headers: dict[str, str] = {}
    for key in ("email", "name", "password"):
        raw = cols.get(key)
        if not isinstance(raw, str) or not raw.strip():
            raise ValueError(f"columns.{key} must be a non-empty string in {path}")
        headers[key] = raw.strip()

    return column_mapping_from_headers(
        headers["email"],
        headers["name"],
        headers["password"],
    )


def resolve_column_mapping(path: Path) -> ColumnMapping:
    """Use YAML when the file exists; otherwise built-in defaults."""
    if path.is_file():
        return load_column_mapping(path)
    return DEFAULT_COLUMN_MAPPING


def delta_path(latest: Path) -> Path:
    """e.g. data/server_registration_import.csv -> data/server_registration_import_delta.csv"""
    return latest.parent / f"{latest.stem}_delta{latest.suffix}"


def netbird_password(raw: str, suffix: str) -> tuple[str, bool]:
    """Return password for NetBird and whether suffix (or suffix+1) was appended."""
    if validate_password_netbird(raw) is None:
        return raw, False
    candidate = raw + suffix
    if validate_password_netbird(candidate) is not None:
        # e.g. missing digit after Aa@ — append 1 while keeping suffix at the end.
        candidate = candidate + "1"
    err = validate_password_netbird(candidate)
    if err:
        raise ValueError(f"password still invalid after suffix {suffix!r}: {err}")
    return candidate, True


def transform_rows(
    rows: list[dict[str, str]],
    *,
    mapping: ColumnMapping,
    suffix: str,
    auto_groups: str,
    role: str,
) -> tuple[list[dict[str, str]], list[dict[str, str]], list[str]]:
    """Build import rows, password report rows, and error messages."""
    import_rows: list[dict[str, str]] = []
    report_rows: list[dict[str, str]] = []
    errors: list[str] = []

    for i, row in enumerate(rows, start=2):
        email = row.get(mapping.email_key, "").strip()
        name = row.get(mapping.name_key, "").strip()
        raw_pwd = row.get(mapping.password_key, "").strip()
        line_ref = f"row {i} ({email or '?'})"

        if not email:
            continue
        if err := validate_email(email):
            errors.append(f"{line_ref}: {err}")
            continue
        if not name:
            errors.append(f"{line_ref}: missing name")
            continue
        if not raw_pwd:
            errors.append(f"{line_ref}: missing password")
            continue

        try:
            password, suffix_applied = netbird_password(raw_pwd, suffix)
        except ValueError as e:
            errors.append(f"{line_ref}: {e}")
            continue

        import_rows.append(
            {
                "email": email,
                "name": name,
                "role": role,
                "password": password,
                "auto_groups": auto_groups,
            }
        )
        report_rows.append(
            {
                "email": email,
                "name": name,
                "password_original": raw_pwd,
                "password_for_netbird": password,
            }
        )
        if suffix_applied:
            print(f"{line_ref}: appended {suffix!r} to password")

    return import_rows, report_rows, errors


def filter_delta_rows(
    rows: list[dict[str, str]], registered_emails: set[str]
) -> list[dict[str, str]]:
    if not registered_emails:
        return list(rows)
    return [
        row
        for row in rows
        if row.get("email", "").strip().lower() not in registered_emails
    ]


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def remove_if_exists(path: Path) -> None:
    if path.is_file():
        path.unlink()


def fetch_registered_emails(base_url: str, token: str) -> set[str]:
    session = session_with_token(token)
    users = fetch_users(session, base_url)
    return existing_emails_from_users(users)


def write_registered_snapshot(path: Path, registered_emails: set[str]) -> None:
    rows = [{"email": email} for email in sorted(registered_emails)]
    write_csv(path, REGISTERED_FIELDNAMES, rows)


def write_delta_outputs(
    *,
    import_rows: list[dict[str, str]],
    report_rows: list[dict[str, str]],
    registered_emails: set[str],
    delta_import: Path,
    delta_passwords: Path,
) -> None:
    delta_import_rows = filter_delta_rows(import_rows, registered_emails)
    delta_report_rows = filter_delta_rows(report_rows, registered_emails)

    if not delta_import_rows:
        remove_if_exists(delta_import)
        remove_if_exists(delta_passwords)
        print("No new submissions.")
        return

    write_csv(delta_import, IMPORT_FIELDNAMES, delta_import_rows)
    write_csv(delta_passwords, REPORT_FIELDNAMES, delta_report_rows)
    print(
        f"Wrote {len(delta_import_rows)} new row(s) to {delta_import} "
        f"and {delta_passwords}"
    )
    for row in delta_import_rows:
        print(f"  new: {row['email']}")


def main(argv: list[str] | None = None) -> int:
    load_dotenv()

    parser = argparse.ArgumentParser(
        description="Convert server registration xlsx to user-manage import CSV.",
        parents=[netbird_connection_parent_parser()],
    )
    parser.add_argument(
        "--input",
        "-i",
        type=Path,
        default=DEFAULT_INPUT,
        help=f"Source xlsx (default: {DEFAULT_INPUT})",
    )
    parser.add_argument(
        "--mapping",
        "-m",
        type=Path,
        default=DEFAULT_MAPPING,
        help=f"YAML column mapping (default: {DEFAULT_MAPPING.name} next to this script)",
    )
    parser.add_argument(
        "--output",
        "-o",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"Import CSV for user-manage (default: {DEFAULT_OUTPUT})",
    )
    parser.add_argument(
        "--password-report",
        type=Path,
        default=DEFAULT_PASSWORD_REPORT,
        help=f"Password mapping CSV (default: {DEFAULT_PASSWORD_REPORT})",
    )
    parser.add_argument(
        "--registered-emails",
        type=Path,
        default=DEFAULT_PRE_EMAILS,
        help=f"NetBird registered email snapshot (default: {DEFAULT_PRE_EMAILS})",
    )
    parser.add_argument(
        "--suffix",
        default=DEFAULT_SUFFIX,
        help=f"Suffix for non-compliant passwords (default: {DEFAULT_SUFFIX!r})",
    )
    parser.add_argument(
        "--auto-groups",
        default=DEFAULT_AUTO_GROUPS,
        help=f"auto_groups column value (default: {DEFAULT_AUTO_GROUPS})",
    )
    parser.add_argument(
        "--role",
        default=DEFAULT_ROLE,
        help=f"role column value (default: {DEFAULT_ROLE})",
    )
    args = parser.parse_args(argv)

    if not args.input.is_file():
        print(f"Input not found: {args.input}", file=sys.stderr)
        return 2

    if not args.token:
        print(
            "Missing PAT: set NETBIRD_TOKEN in .env or pass --token",
            file=sys.stderr,
        )
        return 4

    try:
        mapping = resolve_column_mapping(args.mapping)
    except (ValueError, OSError, yaml.YAMLError) as e:
        print(f"Column mapping error: {e}", file=sys.stderr)
        return 2

    try:
        rows = load_rows(str(args.input))
    except Exception as e:
        print(f"Failed to read {args.input}: {e}", file=sys.stderr)
        return 2

    import_rows, report_rows, errors = transform_rows(
        rows,
        mapping=mapping,
        suffix=args.suffix,
        auto_groups=args.auto_groups,
        role=args.role,
    )

    if errors:
        for msg in errors:
            print(msg, file=sys.stderr)
        return 3

    if not import_rows:
        print("No rows to export.", file=sys.stderr)
        return 3

    delta_import_path = delta_path(args.output)
    delta_passwords_path = delta_path(args.password_report)

    write_csv(args.output, IMPORT_FIELDNAMES, import_rows)
    write_csv(args.password_report, REPORT_FIELDNAMES, report_rows)
    print(f"Wrote {len(import_rows)} row(s) to {args.output}")
    print(f"Wrote password report to {args.password_report}")

    try:
        registered_emails = fetch_registered_emails(args.base_url, args.token)
    except requests.RequestException as e:
        print(f"Failed to fetch NetBird users: {e}", file=sys.stderr)
        return 5

    write_registered_snapshot(args.registered_emails, registered_emails)
    print(
        f"Wrote {len(registered_emails)} registered email(s) to {args.registered_emails}"
    )

    write_delta_outputs(
        import_rows=import_rows,
        report_rows=report_rows,
        registered_emails=registered_emails,
        delta_import=delta_import_path,
        delta_passwords=delta_passwords_path,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
