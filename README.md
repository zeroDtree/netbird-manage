# NetBird user manage

CLI tools for NetBird Management API: bulk users (embedded IdP) and optional per-user groups / machine assignment.

## Quick start

```bash
cp .env.example .env   # NETBIRD_TOKEN (and NETBIRD_API_BASE if self-hosted)
uv sync
```

## Users (`user_manage.py`)

```bash
uv run python user_manage.py import -f example.csv
uv run python user_manage.py delete -f example_delete.csv --yes
```

Input: `.csv` or `.xlsx`; headers are case-insensitive (spaces become underscores). Options: **`uv run python user_manage.py import --help`** and **`… delete --help`**.

Installed wheel: **`uv run netbird-user-manage import|delete …`**.

## Assign (`policy_manage.py`)

Creates per-user **clients** / **servers** NetBird groups, can add a **policy** (clients → servers), and **assign** moves a peer into or out of the user’s **servers** group.

```bash
uv run python policy_manage.py ensure-user-groups --email alice@example.com --create-policy --update-user-auto-groups
uv run python policy_manage.py assign --email alice@example.com --peer-name my-server-host
```

Installed wheel: **`uv run netbird-assign …`**. All flags: **`uv run python policy_manage.py --help`** and per subcommand **`… ensure-user-groups --help`** / **`… assign --help`**.

## HTTP API (`assign_api`, optional)

```bash
uv sync --extra api
export NETBIRD_TOKEN=…              # server only: calls NetBird
export ASSIGN_SERVICE_TOKEN=…     # clients: Bearer for this API
uv run netbird-assign-api         # default http://0.0.0.0:8080
```

Use **`Authorization: Bearer $ASSIGN_SERVICE_TOKEN`** and **`Content-Type: application/json`**. Request/response shapes: **`http://127.0.0.1:8080/docs`** (Swagger UI) while the server is running.

```bash
curl -sS http://127.0.0.1:8080/health
curl -sS -X POST http://127.0.0.1:8080/ensure-user-groups \
  -H "Authorization: Bearer ${ASSIGN_SERVICE_TOKEN}" -H "Content-Type: application/json" \
  -d '{"email":"alice@example.com","create_policy":true,"update_user_auto_groups":true}'
curl -sS -X POST http://127.0.0.1:8080/assign \
  -H "Authorization: Bearer ${ASSIGN_SERVICE_TOKEN}" -H "Content-Type: application/json" \
  -d '{"email":"alice@example.com","peer_name":"my-server-host"}'
curl -sS -X DELETE http://127.0.0.1:8080/assign \
  -H "Authorization: Bearer ${ASSIGN_SERVICE_TOKEN}" -H "Content-Type: application/json" \
  -d '{"email":"alice@example.com","peer_name":"my-server-host"}'
```

**Note:** `auto_groups` applies to every peer under that NetBird user; use **`assign`** (or setup keys) for machines that should live only in the **servers** group.
