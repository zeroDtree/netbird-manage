#!/usr/bin/env python3
"""
Notify users of NetBird login passwords from server_registration_passwords.csv.

Modes:
  --print          Print one message per row to stdout (default).
  --out-dir DIR    Write one UTF-8 text file per email under DIR.
  --send           Send email via SMTP (requires env vars below).

SMTP environment (when using --send); loaded from .env via python-dotenv:
  SMTP_HOST, SMTP_USER, SMTP_PASSWORD, SMTP_PORT, SMTP_FROM, SMTP_SSL, SMTP_USE_TLS
  (see .env.example). Port 994 / 465: set SMTP_SSL=1 and SMTP_USE_TLS=0 (SSL from connect).

Run from repo root:
  uv run python my/notify_netbird_passwords.py --print
  uv run python my/notify_netbird_passwords.py --out-dir data/password_notices --dry-run
  uv run python my/notify_netbird_passwords.py --send --dry-run

  --send reuses one SMTP connection for all recipients; per-recipient failures are logged
  and do not stop the batch. Optional SMTP_DELAY_SECONDS (default 0.5) between messages.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import smtplib
import sys
import time
from contextlib import contextmanager
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
from typing import Any, Iterator

from dotenv import load_dotenv

DEFAULT_CSV = Path("data/server_registration_passwords.csv")
DEFAULT_ERROR_LOG = Path("data/notify_send_errors.jsonl")
DEFAULT_SEND_DELAY = 0.5


def _env(name: str) -> str:
    return os.environ.get(name, "").strip()

# Chinese notice template (plain text).
SUBJECT = "NetBird 账号已开通 — 登录说明"

BODY_TEMPLATE = """{name}，你好：

你的 NetBird 账号已开通，请使用以下信息登录客户端或管理后台。

登录邮箱：{email}
登录密码：{password}

说明：
1. 密码需满足 NetBird 要求：至少 8 位，且包含大写字母、数字和符号（如 @、!）。
2. 若登记表密码已符合要求，则与下方「登录密码」一致；否则我们在原密码末尾做了调整
   （常见为追加 Aa@，少数为 Aa@1）。
3. 请不要将本邮件转发他人。建议首次登录后在 NetBird 中修改为你自己的密码。

如有问题请联系管理员。

此邮件由系统自动发送，请不要直接回复。
"""


def load_password_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        required = {"email", "name", "password_for_netbird"}
        if not reader.fieldnames or not required.issubset(
            {h.strip() for h in reader.fieldnames}
        ):
            raise ValueError(
                f"CSV must have columns: {', '.join(sorted(required))}; "
                f"got {reader.fieldnames}"
            )
        rows: list[dict[str, str]] = []
        for raw in reader:
            email = (raw.get("email") or "").strip()
            name = (raw.get("name") or "").strip()
            password = (raw.get("password_for_netbird") or "").strip()
            if not email:
                continue
            if not name or not password:
                raise ValueError(f"Missing name or password_for_netbird for {email}")
            rows.append(
                {
                    "email": email,
                    "name": name,
                    "password": password,
                    "password_original": (raw.get("password_original") or "").strip(),
                }
            )
        return rows


def build_message(row: dict[str, str], *, subject: str) -> tuple[str, str]:
    body = BODY_TEMPLATE.format(
        name=row["name"],
        email=row["email"],
        password=row["password"],
    )
    return subject, body


def safe_filename(email: str) -> str:
    return re.sub(r"[^\w.\-@]+", "_", email)


def print_notices(rows: list[dict[str, str]], *, subject: str) -> None:
    for i, row in enumerate(rows):
        subj, body = build_message(row, subject=subject)
        if i:
            print("\n" + "=" * 60 + "\n")
        print(f"To: {row['email']}")
        print(f"Subject: {subj}")
        print()
        print(body)


def write_notice_files(
    rows: list[dict[str, str]],
    out_dir: Path,
    *,
    subject: str,
) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    for row in rows:
        subj, body = build_message(row, subject=subject)
        path = out_dir / f"{safe_filename(row['email'])}.txt"
        content = f"To: {row['email']}\nSubject: {subj}\n\n{body}"
        path.write_text(content, encoding="utf-8")
        print(f"Wrote {path}")


def smtp_settings_from_env() -> dict[str, str | int | bool]:
    """Read SMTP config from .env (SMTP_*)."""
    host = _env("SMTP_HOST")
    user = _env("SMTP_USER")
    password = _env("SMTP_PASSWORD")
    from_addr = _env("SMTP_FROM") or user
    port_raw = _env("SMTP_PORT") or "587"
    port = int(port_raw)

    use_ssl_raw = _env("SMTP_SSL")
    if use_ssl_raw:
        use_ssl = use_ssl_raw not in ("0", "false", "no")
    else:
        use_ssl = port in (465, 994)

    use_tls_raw = _env("SMTP_USE_TLS")
    if use_tls_raw:
        use_tls = use_tls_raw not in ("0", "false", "no")
    else:
        use_tls = not use_ssl

    if not host or not user or not password or not from_addr:
        raise ValueError(
            "Set SMTP in .env: SMTP_HOST, SMTP_USER, SMTP_PASSWORD "
            "(and SMTP_PORT, SMTP_FROM as needed) — see .env.example"
        )
    return {
        "host": host,
        "port": port,
        "user": user,
        "password": password,
        "from_addr": from_addr,
        "use_ssl": use_ssl,
        "use_tls": use_tls,
    }


def build_mime_message(
    *,
    from_addr: str,
    to_email: str,
    subject: str,
    body: str,
) -> MIMEMultipart:
    msg = MIMEMultipart()
    msg["From"] = from_addr
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain", "utf-8"))
    return msg


@contextmanager
def smtp_session(smtp: dict[str, str | int | bool]) -> Iterator[smtplib.SMTP]:
    """One TCP/TLS connection and login for the whole batch."""
    host = str(smtp["host"])
    port = int(smtp["port"])
    use_ssl = bool(smtp["use_ssl"])
    use_tls = bool(smtp["use_tls"])

    if use_ssl:
        server: smtplib.SMTP = smtplib.SMTP_SSL(host, port, timeout=60)
    else:
        server = smtplib.SMTP(host, port, timeout=60)

    try:
        if not use_ssl and use_tls:
            server.starttls()
        server.login(str(smtp["user"]), str(smtp["password"]))
        yield server
    finally:
        try:
            server.quit()
        except smtplib.SMTPException:
            pass


def send_with_server(
    server: smtplib.SMTP,
    smtp: dict[str, str | int | bool],
    *,
    to_email: str,
    subject: str,
    body: str,
) -> None:
    from_addr = str(smtp["from_addr"])
    msg = build_mime_message(
        from_addr=from_addr, to_email=to_email, subject=subject, body=body
    )
    server.sendmail(from_addr, [to_email], msg.as_string())


def append_send_error(path: Path, record: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


def send_delay_seconds(cli_delay: float | None) -> float:
    if cli_delay is not None:
        return max(0.0, cli_delay)
    raw = _env("SMTP_DELAY_SECONDS")
    if raw:
        try:
            return max(0.0, float(raw))
        except ValueError:
            pass
    return DEFAULT_SEND_DELAY


def send_notices(
    rows: list[dict[str, str]],
    *,
    subject: str,
    dry_run: bool,
    delay_seconds: float,
    error_log: Path,
) -> tuple[int, int]:
    """Send all notices. Returns (ok_count, failed_count)."""
    if dry_run:
        for row in rows:
            subj, _ = build_message(row, subject=subject)
            print(f"[dry-run] would send to {row['email']}: {subj}")
        return 0, 0

    smtp = smtp_settings_from_env()
    ok = 0
    failed = 0

    with smtp_session(smtp) as server:
        for i, row in enumerate(rows):
            to_email = row["email"]
            try:
                subj, body = build_message(row, subject=subject)
                send_with_server(
                    server, smtp, to_email=to_email, subject=subj, body=body
                )
                ok += 1
                print(f"Sent to {to_email}")
            except (smtplib.SMTPException, OSError, ValueError) as e:
                failed += 1
                err_msg = str(e)
                print(f"Failed {to_email}: {err_msg}", file=sys.stderr)
                append_send_error(
                    error_log,
                    {"email": to_email, "name": row.get("name", ""), "error": err_msg},
                )

            if delay_seconds > 0 and i < len(rows) - 1:
                time.sleep(delay_seconds)

    print(f"Send summary: ok={ok} failed={failed}", file=sys.stderr)
    if failed:
        print(f"Failures logged to {error_log}", file=sys.stderr)
    return ok, failed


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Notify users of NetBird passwords from server_registration_passwords.csv."
    )
    parser.add_argument(
        "--csv",
        type=Path,
        default=DEFAULT_CSV,
        help=f"Password mapping CSV (default: {DEFAULT_CSV})",
    )
    parser.add_argument(
        "--subject",
        default=SUBJECT,
        help="Email subject line",
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--print",
        action="store_true",
        help="Print messages to stdout (default if no other mode)",
    )
    mode.add_argument(
        "--out-dir",
        type=Path,
        metavar="DIR",
        help="Write one .txt notice per email under DIR",
    )
    mode.add_argument(
        "--send",
        action="store_true",
        help="Send email via SMTP (env: SMTP_HOST, SMTP_USER, SMTP_PASSWORD, ...)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Only valid with --send: list recipients without sending",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=None,
        metavar="SECONDS",
        help=(
            "Pause between messages when using --send (default: SMTP_DELAY_SECONDS "
            f"or {DEFAULT_SEND_DELAY})"
        ),
    )
    parser.add_argument(
        "--error-log",
        type=Path,
        default=DEFAULT_ERROR_LOG,
        help=f"Append per-recipient send failures as JSONL (default: {DEFAULT_ERROR_LOG})",
    )
    parser.add_argument(
        "--exclude-email",
        action="append",
        default=[],
        metavar="EMAIL",
        help="Skip this address (repeatable), e.g. test accounts",
    )
    parser.add_argument(
        "--only-email",
        action="append",
        default=[],
        metavar="EMAIL",
        help="Send/print only these addresses (repeatable); for SMTP smoke tests",
    )
    args = parser.parse_args(argv)

    if args.dry_run and not args.send:
        parser.error("--dry-run requires --send")

    if args.send:
        load_dotenv()

    if not args.csv.is_file():
        print(f"CSV not found: {args.csv}", file=sys.stderr)
        return 2

    try:
        rows = load_password_rows(args.csv)
    except (ValueError, OSError) as e:
        print(f"Error: {e}", file=sys.stderr)
        return 2

    exclude = {e.strip().lower() for e in args.exclude_email}
    rows = [r for r in rows if r["email"].lower() not in exclude]

    only = {e.strip().lower() for e in args.only_email}
    if only:
        rows = [r for r in rows if r["email"].lower() in only]
        missing = only - {r["email"].lower() for r in rows}
        if missing:
            print(
                "Warning: --only-email not found in CSV: "
                + ", ".join(sorted(missing)),
                file=sys.stderr,
            )

    if not rows:
        print("No rows to notify.", file=sys.stderr)
        return 3

    try:
        if args.out_dir is not None:
            write_notice_files(rows, args.out_dir, subject=args.subject)
        elif args.send:
            delay = send_delay_seconds(args.delay)
            ok, failed = send_notices(
                rows,
                subject=args.subject,
                dry_run=args.dry_run,
                delay_seconds=delay,
                error_log=args.error_log,
            )
            if not args.dry_run and failed:
                return 1
            if not args.dry_run:
                print(f"Done: sent={ok} failed={failed}", file=sys.stderr)
                return 0
        else:
            print_notices(rows, subject=args.subject)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 4
    except (smtplib.SMTPException, OSError) as e:
        print(f"SMTP connection/login error: {e}", file=sys.stderr)
        return 5

    print(f"Done: {len(rows)} recipient(s).", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
