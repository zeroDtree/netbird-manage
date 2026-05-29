# NetBird user manage

CLI tools for NetBird Management API: bulk users (embedded IdP) and optional per-user groups / machine assignment.

## Quick start

```bash
cp .env.example .env   # NETBIRD_TOKEN (and NETBIRD_API_BASE if self-hosted)
uv sync
```

## Users

```bash
uv run user-manage import -f examples/users.csv
uv run user-manage delete -f examples/users_to_delete.csv --yes
```

Input: `.csv` or `.xlsx`; headers are case-insensitive (spaces become underscores). 

For all flags and options, run 
- **`uv run user-manage import --help`**
- **`uv run user-manage delete --help`**.

## Server registration spreadsheet

Convert [`data/服务器申请登记.xlsx`](data/服务器申请登记.xlsx) to import CSV with [`my/prepare_server_registration_import.py`](my/prepare_server_registration_import.py). Spreadsheet column headers are configured in [`my/server_registration_columns.yaml`](my/server_registration_columns.yaml) (override with `--mapping`). Passwords that fail NetBird rules get **`Aa@`** appended (and **`1`** after that if a digit is still missing). Each user is assigned shared group **`client_group`** via the `auto_groups` column.

Each prepare run fetches registered emails from NetBird and writes `*_delta.csv` with spreadsheet rows not yet in NetBird. Requires `NETBIRD_TOKEN` in `.env`. Use the delta files for import and password notify. See [`my/README.md`](my/README.md) for notify scripts and security notes.

```bash
uv run python my/prepare_server_registration_import.py

uv run user-manage import \
  -f data/server_registration_import_delta.csv \
  --resolve-group-names \
  --dry-run

uv run user-manage import \
  -f data/server_registration_import_delta.csv \
  --resolve-group-names
```

Outputs (gitignored under `data/`): latest full export, `pre_server_registration_emails.csv` (NetBird snapshot), and `*_delta.csv` for pending registrations. Ensure group **`client_group`** exists in NetBird before import.

## Groups and server peers

Creates per-user **clients** / **servers** NetBird groups, can add a **policy** (clients → servers), and **manage-server-peer** moves a peer into or out of the user’s **servers** group. **remove-user-groups** tears down those groups (and optional policy / auto_groups changes).

```bash
# Per-user clients/servers groups, pairing policy, and clients group in auto_groups.
uv run policy-manage ensure-user-groups \
  --email alice@example.com \
  --create-policy \
  --add-client-group-to-auto-groups

# Put a server machine (peer) into that user's servers group (hostname must match exactly).
uv run policy-manage manage-server-peer \
  --email alice@example.com \
  --peer-name my-server-host

# Preview teardown (no NetBird writes).
uv run policy-manage remove-user-groups \
  --email alice@example.com \
  --dry-run

# Delete groups and pairing policy (requires --yes).
uv run policy-manage remove-user-groups \
  --email alice@example.com \
  --yes
```

For all options: **`uv run policy-manage --help`**. For one subcommand only: 
- **`uv run policy-manage ensure-user-groups --help`**
- **`uv run policy-manage remove-user-groups --help`**
- **`uv run policy-manage manage-server-peer --help`**.

## HTTP API (optional)

Thin HTTP wrapper around the same flows as **`policy-manage`**: callers send a service Bearer token; the server uses **`NETBIRD_TOKEN`** to call NetBird.

**Install and run** (default listen **`0.0.0.0:8080`**; override with **`ASSIGN_API_HOST`** / **`ASSIGN_API_PORT`**):

```bash
uv sync --all-groups --extra api
export NETBIRD_TOKEN=YOUR_NETBIRD_PAT          # server → NetBird Management API
export ASSIGN_SERVICE_TOKEN=YOUR_SERVICE_TOKEN # clients → this API (Bearer)
uv run expose-api
```

**Clients:** send **`Authorization: Bearer $ASSIGN_SERVICE_TOKEN`** and **`Content-Type: application/json`**. While the server is up, OpenAPI is at **`http://127.0.0.1:8080/docs`** (adjust host/port if you changed them).

**Examples** (`API_BASE` matches where you bound the server):

```bash
API_BASE=http://127.0.0.1:8080

curl -sS "$API_BASE/health"

curl -sS -X POST "$API_BASE/ensure-user-groups" \
  -H "Authorization: Bearer ${ASSIGN_SERVICE_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"email":"alice@example.com","create_policy":true,"add_client_group_to_auto_groups":true}'

curl -sS -X POST "$API_BASE/manage-server-peer" \
  -H "Authorization: Bearer ${ASSIGN_SERVICE_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"email":"alice@example.com","peer_name":"my-server-host"}'

curl -sS -X DELETE "$API_BASE/manage-server-peer" \
  -H "Authorization: Bearer ${ASSIGN_SERVICE_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"email":"alice@example.com","peer_name":"my-server-host"}'

curl -sS -X DELETE "$API_BASE/remove-user-groups" \
  -H "Authorization: Bearer ${ASSIGN_SERVICE_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"email":"alice@example.com","dry_run":true}'

curl -sS -X DELETE "$API_BASE/remove-user-groups" \
  -H "Authorization: Bearer ${ASSIGN_SERVICE_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"email":"alice@example.com"}'
```

**Note:** NetBird **`auto_groups`** applies to every peer under that user. For devices that should be **servers only** (members of the **servers** group), use **`manage-server-peer`** or setup keys—not only default auto-group behavior.