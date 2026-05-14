#!/usr/bin/env python3
"""HTTP API for NetBird machine assignment (wraps assign_core)."""

from __future__ import annotations

import os
import sys

try:
    from dotenv import load_dotenv
    from fastapi import Depends, FastAPI, HTTPException, status
    from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
    from pydantic import BaseModel, Field
except ImportError:
    print("Install API extras: uv sync --extra api", file=sys.stderr)
    raise

from assign_core import assign_peer_to_user_servers, ensure_user_groups_and_policy
from netbird_cli import DEFAULT_API_BASE
from netbird_client import session_with_token

app = FastAPI(title="NetBird assign API", version="0.1.0")
_bearer = HTTPBearer(auto_error=False)


def _service_token() -> str:
    return os.environ.get("ASSIGN_SERVICE_TOKEN", "").strip()


def _nb_token() -> str:
    t = os.environ.get("NETBIRD_TOKEN", "").strip()
    if not t:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="NETBIRD_TOKEN is not configured on the server",
        )
    return t


def _nb_base() -> str:
    return os.environ.get("NETBIRD_API_BASE", DEFAULT_API_BASE).rstrip("/")


def verify_bearer(
    creds: HTTPAuthorizationCredentials | None = Depends(_bearer),
) -> None:
    expected = _service_token()
    if not expected:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="ASSIGN_SERVICE_TOKEN is not set",
        )
    if creds is None or creds.scheme.lower() != "bearer":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing Bearer token",
        )
    if creds.credentials != expected:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )


class EnsureBody(BaseModel):
    email: str = Field(..., min_length=3)
    name_prefix: str = Field(default_factory=lambda: os.environ.get("NETBIRD_ASSIGN_NAME_PREFIX", "nb"))
    create_policy: bool = False
    bidirectional: bool = False
    update_user_auto_groups: bool = False
    dry_run: bool = False


class AssignBody(BaseModel):
    email: str = Field(..., min_length=3)
    peer_id: str | None = None
    peer_name: str | None = None
    name_prefix: str = Field(default_factory=lambda: os.environ.get("NETBIRD_ASSIGN_NAME_PREFIX", "nb"))
    dry_run: bool = False


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/ensure-user-groups", dependencies=[Depends(verify_bearer)])
def api_ensure(body: EnsureBody) -> dict:
    session = session_with_token(_nb_token())
    out = ensure_user_groups_and_policy(
        session,
        _nb_base(),
        body.email,
        name_prefix=body.name_prefix,
        create_policy=body.create_policy,
        bidirectional=body.bidirectional,
        update_user_auto_groups=body.update_user_auto_groups,
        dry_run=body.dry_run,
    )
    if not out.get("ok"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=out.get("error", "ensure failed"),
        )
    return out


@app.post("/assign", dependencies=[Depends(verify_bearer)])
def api_assign(body: AssignBody) -> dict:
    if not body.peer_id and not body.peer_name:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="peer_id or peer_name is required",
        )
    session = session_with_token(_nb_token())
    res = assign_peer_to_user_servers(
        session,
        _nb_base(),
        body.email,
        name_prefix=body.name_prefix,
        peer_id=body.peer_id,
        peer_name=body.peer_name,
        remove=False,
        dry_run=body.dry_run,
    )
    if not res.get("ok") and "ambiguous" in str(res.get("error", "")).lower():
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=res.get("error", "ambiguous peer"),
        )
    if not res.get("ok"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=res.get("error", "assign failed"),
        )
    return res


@app.delete("/assign", dependencies=[Depends(verify_bearer)])
def api_unassign(body: AssignBody) -> dict:
    if not body.peer_id and not body.peer_name:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="peer_id or peer_name is required",
        )
    session = session_with_token(_nb_token())
    res = assign_peer_to_user_servers(
        session,
        _nb_base(),
        body.email,
        name_prefix=body.name_prefix,
        peer_id=body.peer_id,
        peer_name=body.peer_name,
        remove=True,
        dry_run=body.dry_run,
    )
    if not res.get("ok"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=res.get("error", "unassign failed"),
        )
    return res


def main() -> None:
    load_dotenv()
    import uvicorn

    host = os.environ.get("ASSIGN_API_HOST", "0.0.0.0")
    port = int(os.environ.get("ASSIGN_API_PORT", "8080"))
    uvicorn.run("assign_api:app", host=host, port=port, reload=False)


if __name__ == "__main__":
    main()
