"""NetBird Management API: peer lookup helpers."""

from __future__ import annotations

from urllib.parse import quote

import requests

from netbird_client import api_url, request_with_retry, response_status


def resolve_peer_id(
    session: requests.Session,
    base: str,
    *,
    peer_id: str | None,
    peer_name: str | None,
) -> tuple[str | None, str | None]:
    """Return (peer_id, error_message)."""
    if peer_id and peer_id.strip():
        pid = peer_id.strip()
        path = f"/api/peers/{quote(pid, safe='')}"
        url = api_url(base, path)
        r = request_with_retry(session, "GET", url, headers={"Accept": "application/json"})
        if response_status(r) == 404:
            return None, f"no peer with id {pid!r}"
        r.raise_for_status()
        data = r.json()
        if isinstance(data, dict) and data.get("id"):
            return str(data["id"]), None
        return None, "GET peer: invalid response"

    name = (peer_name or "").strip()
    if not name:
        return None, "peer_id or peer_name is required"

    url = api_url(base, f"/api/peers?name={quote(name, safe='')}")
    r = request_with_retry(session, "GET", url, headers={"Accept": "application/json"})
    r.raise_for_status()
    data = r.json()
    if not isinstance(data, list):
        return None, "GET /api/peers: expected list"
    exact = [p for p in data if isinstance(p, dict) and str(p.get("name", "")) == name]
    if len(exact) == 0:
        return None, f"no peer with exact name {name!r}"
    if len(exact) > 1:
        return None, (
            f"ambiguous peer name {name!r}: {len(exact)} matches; pass peer_id"
        )
    pid = exact[0].get("id")
    if not pid:
        return None, "peer record has no id"
    return str(pid), None
