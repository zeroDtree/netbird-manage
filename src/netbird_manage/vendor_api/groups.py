"""NetBird Management API: network group helpers."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import requests

from ..utils.client import (
    api_url,
    json_headers,
    request_with_retry,
    response_status,
)


def fetch_groups_map(session: requests.Session, base: str) -> dict[str, str]:
    """Lowercased group name -> id."""
    url = api_url(base, "/api/groups")
    r = request_with_retry(session, "GET", url, headers={"Accept": "application/json"})
    r.raise_for_status()
    data = r.json()
    m: dict[str, str] = {}
    if not isinstance(data, list):
        return m
    for g in data:
        if not isinstance(g, dict):
            continue
        gid = g.get("id")
        name = g.get("name")
        if gid and name:
            key = str(name).strip().lower()
            if key not in m:
                m[key] = str(gid)
    return m


def find_group_id_by_exact_name(
    session: requests.Session, base: str, name: str
) -> str | None:
    url = api_url(base, f"/api/groups?name={quote(name, safe='')}")
    r = request_with_retry(session, "GET", url, headers={"Accept": "application/json"})
    # Some management APIs return 404 when the name filter matches no group instead of 200 + [].
    if response_status(r) == 404:
        return None
    r.raise_for_status()
    data = r.json()
    if not isinstance(data, list):
        return None
    for g in data:
        if isinstance(g, dict) and g.get("name") == name and g.get("id"):
            return str(g["id"])
    return None


def create_group(
    session: requests.Session, base: str, name: str, *, dry_run: bool
) -> tuple[str | None, str]:
    if dry_run:
        return None, f"would POST /api/groups name={name!r}"
    url = api_url(base, "/api/groups")
    r = request_with_retry(
        session,
        "POST",
        url,
        headers=json_headers(),
        json_body={"name": name},
    )
    if response_status(r) >= 400:
        return None, f"create group failed: {response_status(r)} {r.text[:500]}"
    try:
        payload = r.json()
    except json.JSONDecodeError:
        return None, "create group failed: invalid JSON"
    gid = payload.get("id") if isinstance(payload, dict) else None
    if not gid:
        return None, "create group failed: no id in response"
    return str(gid), "created"


def fetch_group(session: requests.Session, base: str, group_id: str) -> dict[str, Any]:
    path = f"/api/groups/{quote(group_id, safe='')}"
    url = api_url(base, path)
    r = request_with_retry(session, "GET", url, headers={"Accept": "application/json"})
    r.raise_for_status()
    data = r.json()
    if not isinstance(data, dict):
        raise RuntimeError("GET /api/groups/{id}: expected object")
    return data


def put_group_peers_and_resources(
    session: requests.Session,
    base: str,
    group_id: str,
    *,
    name: str,
    peer_ids: list[str],
    resources: list[dict[str, Any]],
) -> requests.Response:
    path = f"/api/groups/{quote(group_id, safe='')}"
    url = api_url(base, path)
    body: dict[str, Any] = {
        "name": name,
        "peers": peer_ids,
        "resources": resources,
    }
    return request_with_retry(
        session,
        "PUT",
        url,
        headers=json_headers(),
        json_body=body,
    )


def peer_ids_from_group_dict(group: dict[str, Any]) -> list[str]:
    peers = group.get("peers")
    if not isinstance(peers, list):
        return []
    out: list[str] = []
    for p in peers:
        if isinstance(p, dict) and p.get("id"):
            out.append(str(p["id"]))
        elif isinstance(p, str):
            out.append(p)
    return out


def resources_from_group_dict(group: dict[str, Any]) -> list[dict[str, Any]]:
    res = group.get("resources")
    if not isinstance(res, list):
        return []
    norm: list[dict[str, Any]] = []
    for item in res:
        if isinstance(item, dict) and item.get("id") and item.get("type"):
            norm.append({"id": str(item["id"]), "type": str(item["type"])})
    return norm


def delete_group(
    session: requests.Session, base: str, group_id: str
) -> tuple[bool, str]:
    """DELETE /api/groups/{id}. Returns (ok, message). 404 is treated as success."""
    path = f"/api/groups/{quote(group_id, safe='')}"
    url = api_url(base, path)
    r = request_with_retry(session, "DELETE", url, headers={"Accept": "application/json"})
    code = response_status(r)
    if code == 404:
        return True, "group already absent (404)"
    if code >= 400:
        return False, f"delete group failed: {code} {r.text[:500]}"
    return True, "group deleted"
