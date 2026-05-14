"""NetBird Management API: user account helpers."""

from __future__ import annotations

from typing import Any
from urllib.parse import quote

import requests

from netbird_client import api_url, json_headers, request_with_retry


def fetch_users(session: requests.Session, base: str) -> list[dict[str, Any]]:
    """Return user objects from GET /api/users."""
    url = api_url(base, "/api/users")
    r = request_with_retry(session, "GET", url, headers={"Accept": "application/json"})
    r.raise_for_status()
    data = r.json()
    if not isinstance(data, list):
        return []
    return [u for u in data if isinstance(u, dict)]


def user_by_email(users: list[dict[str, Any]], email: str) -> dict[str, Any] | None:
    el = email.strip().lower()
    for u in users:
        if str(u.get("email", "")).strip().lower() == el:
            return u
    return None


def existing_emails_from_users(users: list[dict[str, Any]]) -> set[str]:
    """Lowercased emails present in the user list."""
    out: set[str] = set()
    for u in users:
        if u.get("email"):
            out.add(str(u["email"]).strip().lower())
    return out


def email_to_user_id(users: list[dict[str, Any]]) -> dict[str, str]:
    """Lowercased email -> NetBird user id (first occurrence wins)."""
    m: dict[str, str] = {}
    for u in users:
        e = u.get("email")
        uid = u.get("id")
        if e and uid:
            key = str(e).strip().lower()
            if key not in m:
                m[key] = str(uid)
    return m


def delete_user_by_id(
    session: requests.Session, base: str, user_id: str
) -> requests.Response:
    path = f"/api/users/{quote(user_id, safe='')}"
    url = api_url(base, path)
    return request_with_retry(
        session,
        "DELETE",
        url,
        headers={"Accept": "application/json"},
    )


def put_user_auto_groups(
    session: requests.Session,
    base: str,
    user_id: str,
    *,
    role: str,
    is_blocked: bool,
    auto_groups: list[str],
) -> requests.Response:
    path = f"/api/users/{quote(user_id, safe='')}"
    url = api_url(base, path)
    return request_with_retry(
        session,
        "PUT",
        url,
        headers=json_headers(),
        json_body={
            "role": role,
            "is_blocked": is_blocked,
            "auto_groups": auto_groups,
        },
    )
