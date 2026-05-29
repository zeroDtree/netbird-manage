# Scripts (`my/`)

Helper scripts for server-registration onboarding. Not part of the `netbird_manage` Python package (installed via `uv sync`, run with `uv run python my/...`).

**Do not commit** real spreadsheets, password CSVs, or `.env` under `data/` — they are gitignored and may contain personal data and plaintext passwords.

## Server registration → NetBird import

[`prepare_server_registration_import.py`](prepare_server_registration_import.py) converts `data/服务器申请登记.xlsx` into CSV files under `data/` for `user-manage import`.

### Column mapping (YAML)

Spreadsheet headers are mapped in [`server_registration_columns.yaml`](server_registration_columns.yaml):

```yaml
columns:
  email: "邮箱（用作netbird登录账号）"
  name: "申请人真实姓名"
  password: "netbird初始登录密码"
```

Values must match Excel header text (normalized the same way as `user-manage` import: lowercase, spaces → underscores). Use a different file with `--mapping` / `-m`. If the default YAML file is missing, built-in defaults matching the above are used.

Each run writes a full export from the xlsx, fetches **already registered emails** from NetBird (`GET /api/users`), and writes `*_delta.csv` with spreadsheet rows whose email is not yet in NetBird. Re-running prepare without xlsx changes keeps the same delta (unlike CSV rotation).

Requires `NETBIRD_TOKEN` in repo-root `.env` (same as `user-manage`).

```bash
# From repo root — sync latest xlsx from WPS first
uv run python my/prepare_server_registration_import.py

# Custom column mapping
uv run python my/prepare_server_registration_import.py -m path/to/columns.yaml

# Import and notify using delta only
uv run user-manage import -f data/server_registration_import_delta.csv \
  --resolve-group-names --dry-run
uv run user-manage import -f data/server_registration_import_delta.csv \
  --resolve-group-names
```

Generated CSVs contain plaintext passwords and are gitignored (see repo `.gitignore`).

| File | Role |
|------|------|
| `server_registration_import.csv` | Latest full export from xlsx |
| `server_registration_passwords.csv` | Latest password mapping |
| `pre_server_registration_emails.csv` | NetBird registered emails (snapshot) |
| `server_registration_*_delta.csv` | Rows in xlsx not yet in NetBird |

If import succeeded but notify failed, delta will no longer include that user (already in NetBird). Notify manually with `--only-email` and the full passwords CSV.

## Notify users of NetBird passwords

[`notify_netbird_passwords.py`](notify_netbird_passwords.py) reads a password CSV (default or `--csv`) and builds a short Chinese notice per user.

```bash
# Preview delta notices in the terminal
uv run python my/notify_netbird_passwords.py --print \
  --csv data/server_registration_passwords_delta.csv

# One .txt file per email (copy into WeCom / manual send)
uv run python my/notify_netbird_passwords.py --out-dir data/password_notices \
  --csv data/server_registration_passwords_delta.csv

# Skip test accounts
uv run python my/notify_netbird_passwords.py --print --exclude-email yyy@qq.com \
  --csv data/server_registration_passwords_delta.csv

# Send via SMTP: add SMTP_* to repo-root .env (see .env.example)
# One SMTP connection for the whole batch; per-recipient failures are logged and skipped.
uv run python my/notify_netbird_passwords.py --send --dry-run \
  --csv data/server_registration_passwords_delta.csv
uv run python my/notify_netbird_passwords.py --send \
  --csv data/server_registration_passwords_delta.csv
```

`--dry-run` only works with `--send`. Optional `SMTP_DELAY_SECONDS=0.5` in `.env` (or `--delay`).
Failed sends append to `data/notify_send_errors.jsonl`.

**SMTP smoke test (one recipient):**

```bash
# Uses data/test_notify_self.csv (single row for your QQ mailbox)
uv run python my/notify_netbird_passwords.py --send --dry-run \
  --csv data/test_notify_self.csv --only-email you@example.com

uv run python my/notify_netbird_passwords.py --send \
  --csv data/test_notify_self.csv --only-email you@example.com
```

`.env` example (994 = SSL, not STARTTLS):

```bash
SMTP_USER=you@example.com
SMTP_HOST=smtphz.qiye.163.com
SMTP_PORT=994
SMTP_PASSWORD=your-authorization-password
SMTP_SSL=1
SMTP_USE_TLS=0
```
