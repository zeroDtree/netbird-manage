"""NetBird Management API: access policy helpers."""

from __future__ import annotations

from typing import Any
from urllib.parse import quote

import requests

from ..utils.client import (
    api_url,
    json_headers,
    request_with_retry,
    response_status,
)


def fetch_policies(session: requests.Session, base: str) -> list[dict[str, Any]]:
    url = api_url(base, "/api/policies")
    r = request_with_retry(session, "GET", url, headers={"Accept": "application/json"})
    r.raise_for_status()
    data = r.json()
    if not isinstance(data, list):
        return []
    return [p for p in data if isinstance(p, dict)]


def ensure_pairing_policy(
    session: requests.Session,
    base: str,
    *,
    policy_name_value: str,
    client_group_id: str,
    server_group_id: str,
    bidirectional: bool,
    dry_run: bool,
) -> tuple[bool, str]:
    policies = fetch_policies(session, base)
    existing = next((p for p in policies if p.get("name") == policy_name_value), None)
    if existing and isinstance(existing, dict):
        return True, "policy already exists (skipped)"

    if dry_run:
        return True, f"would POST /api/policies name={policy_name_value!r}"

    body: dict[str, Any] = {
        "name": policy_name_value,
        "description": "User-scoped access: clients group may reach servers group.",
        "enabled": True,
        "rules": [
            {
                "name": "clients-to-servers",
                "description": "Allow user client peers to reach user server peers",
                "enabled": True,
                "action": "accept",
                "bidirectional": bidirectional,
                "protocol": "all",
                "sources": [client_group_id],
                "destinations": [server_group_id],
            }
        ],
    }
    url = api_url(base, "/api/policies")
    r = request_with_retry(session, "POST", url, headers=json_headers(), json_body=body)
    if response_status(r) >= 400:
        return False, f"create policy failed: {response_status(r)} {r.text[:500]}"
    return True, "policy created"


def delete_policy(
    session: requests.Session, base: str, policy_id: str
) -> tuple[bool, str]:
    """DELETE /api/policies/{id}. Returns (ok, message). 404 is treated as success."""
    path = f"/api/policies/{quote(policy_id, safe='')}"
    url = api_url(base, path)
    r = request_with_retry(session, "DELETE", url, headers={"Accept": "application/json"})
    code = response_status(r)
    if code == 404:
        return True, "policy already absent (404)"
    if code >= 400:
        return False, f"delete policy failed: {code} {r.text[:500]}"
    return True, "policy deleted"
