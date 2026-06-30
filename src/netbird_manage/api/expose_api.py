#!/usr/bin/env python3
"""HTTP API for NetBird machine assignment (wraps assign_core)."""

from __future__ import annotations

import os
import sys

try:
    from fastapi import Depends, FastAPI, HTTPException, status
    from pydantic import BaseModel, Field
except ImportError:
    print("Install API extras: uv sync --extra api", file=sys.stderr)
    raise

from ..services.assign_core import (
    assign_peer_to_user_servers,
    ensure_user_groups_and_policy,
    remove_user_groups_and_policy,
)
from ..utils.cli import load_netbird_env
from ..utils.client import session_with_token
from .deps import netbird_base, netbird_token, verify_bearer

app = FastAPI(title="NetBird assign API", version="0.1.0")


class EnsureBody(BaseModel):
    email: str = Field(..., min_length=3)
    name_prefix: str = Field(default_factory=lambda: os.environ.get("NETBIRD_ASSIGN_NAME_PREFIX", "nb"))
    create_policy: bool = False
    bidirectional: bool = False
    add_client_group_to_auto_groups: bool = False
    dry_run: bool = False


class ManageServerPeerBody(BaseModel):
    email: str = Field(..., min_length=3)
    peer_id: str | None = None
    peer_name: str | None = None
    name_prefix: str = Field(default_factory=lambda: os.environ.get("NETBIRD_ASSIGN_NAME_PREFIX", "nb"))
    dry_run: bool = False


class RemoveUserGroupsBody(BaseModel):
    email: str = Field(..., min_length=3)
    name_prefix: str = Field(default_factory=lambda: os.environ.get("NETBIRD_ASSIGN_NAME_PREFIX", "nb"))
    dry_run: bool = False
    skip_policy_delete: bool = False
    keep_client_in_auto_groups: bool = False


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/ensure-user-groups", dependencies=[Depends(verify_bearer)])
def api_ensure(body: EnsureBody) -> dict:
    session = session_with_token(netbird_token())
    out = ensure_user_groups_and_policy(
        session,
        netbird_base(),
        body.email,
        name_prefix=body.name_prefix,
        create_policy=body.create_policy,
        bidirectional=body.bidirectional,
        add_client_group_to_auto_groups=body.add_client_group_to_auto_groups,
        dry_run=body.dry_run,
    )
    if not out.get("ok"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=out.get("error", "ensure failed"),
        )
    return out


@app.delete("/remove-user-groups", dependencies=[Depends(verify_bearer)])
def api_remove_user_groups(body: RemoveUserGroupsBody) -> dict:
    session = session_with_token(netbird_token())
    out = remove_user_groups_and_policy(
        session,
        netbird_base(),
        body.email,
        name_prefix=body.name_prefix,
        remove_policy=not body.skip_policy_delete,
        strip_client_auto_group=not body.keep_client_in_auto_groups,
        dry_run=body.dry_run,
    )
    if not out.get("ok"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=out.get("error", "remove-user-groups failed"),
        )
    return out


@app.post("/manage-server-peer", dependencies=[Depends(verify_bearer)])
def api_manage_server_peer_add(body: ManageServerPeerBody) -> dict:
    if not body.peer_id and not body.peer_name:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="peer_id or peer_name is required",
        )
    session = session_with_token(netbird_token())
    res = assign_peer_to_user_servers(
        session,
        netbird_base(),
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
            detail=res.get("error", "manage-server-peer failed"),
        )
    return res


@app.delete("/manage-server-peer", dependencies=[Depends(verify_bearer)])
def api_manage_server_peer_remove(body: ManageServerPeerBody) -> dict:
    if not body.peer_id and not body.peer_name:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="peer_id or peer_name is required",
        )
    session = session_with_token(netbird_token())
    res = assign_peer_to_user_servers(
        session,
        netbird_base(),
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
            detail=res.get("error", "manage-server-peer remove failed"),
        )
    return res


def main() -> None:
    load_netbird_env()
    import uvicorn

    host = os.environ.get("ASSIGN_API_HOST", "0.0.0.0")
    port = int(os.environ.get("ASSIGN_API_PORT", "8080"))
    uvicorn.run("netbird_manage.api.expose_api:app", host=host, port=port, reload=False)


if __name__ == "__main__":
    main()
