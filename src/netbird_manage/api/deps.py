"""FastAPI dependencies: service Bearer auth and NetBird server configuration."""

from __future__ import annotations

import os

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from ..utils.cli import DEFAULT_API_BASE

http_bearer = HTTPBearer(auto_error=False)


def service_token() -> str:
    return os.environ.get("ASSIGN_SERVICE_TOKEN", "").strip()


def netbird_token() -> str:
    token = os.environ.get("NETBIRD_TOKEN", "").strip()
    if not token:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="NETBIRD_TOKEN is not configured on the server",
        )
    return token


def netbird_base() -> str:
    return os.environ.get("NETBIRD_API_BASE", DEFAULT_API_BASE).rstrip("/")


def verify_bearer(
    creds: HTTPAuthorizationCredentials | None = Depends(http_bearer),
) -> None:
    expected = service_token()
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
