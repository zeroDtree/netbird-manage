"""NetBird per-user client/server groups, pairing policy, and peer assignment (core logic)."""

from __future__ import annotations

import hashlib
import re
from typing import Any

import requests

from ..utils.client import response_status
from ..utils.netbird_validation import validate_email
from ..vendor_api.groups import (
    create_group,
    delete_group,
    fetch_group,
    find_group_id_by_exact_name,
    peer_ids_from_group_dict,
    put_group_peers_and_resources,
    resources_from_group_dict,
)
from ..vendor_api.peers import resolve_peer_id
from ..vendor_api.policies import delete_policy, ensure_pairing_policy, fetch_policies
from ..vendor_api.users import (
    fetch_users,
    put_user_auto_groups,
    user_by_email,
)


def user_slug(email: str, *, max_len: int = 48) -> str:
    """Stable filesystem-safe slug from email (shortened if too long)."""
    e = email.strip().lower()
    local, _, domain = e.partition("@")
    raw = f"{local}-{domain}"
    safe = re.sub(r"[^a-z0-9_-]+", "-", raw).strip("-")
    if not safe:
        safe = hashlib.sha256(e.encode()).hexdigest()[:16]
    if len(safe) > max_len:
        digest = hashlib.sha256(e.encode()).hexdigest()[:16]
        safe = f"{safe[: max_len - 17]}-{digest}"
    return safe[:max_len]


def _name_prefix(prefix: str) -> str:
    p = (prefix or "").strip()
    if not p:
        p = "nb"
    p = p.rstrip("-")
    return f"{p}-"


def client_server_group_names(slug: str, prefix: str) -> tuple[str, str]:
    p = _name_prefix(prefix)
    return f"{p}{slug}-clients", f"{p}{slug}-servers"


def policy_name(slug: str, prefix: str) -> str:
    p = _name_prefix(prefix)
    return f"{p}{slug}-user-access"


def ensure_user_groups_and_policy(
    session: requests.Session,
    base: str,
    email: str,
    *,
    name_prefix: str,
    create_policy: bool,
    bidirectional: bool,
    add_client_group_to_auto_groups: bool,
    dry_run: bool,
) -> dict[str, Any]:
    """Create client/server groups; optionally pairing policy and user auto_groups."""
    err = validate_email(email)
    if err:
        return {"ok": False, "error": err, "email": email}

    users = fetch_users(session, base)
    u = user_by_email(users, email)
    if not u:
        return {"ok": False, "error": "no user with this email", "email": email}

    user_id = str(u.get("id", ""))
    if not user_id:
        return {"ok": False, "error": "user has no id", "email": email}

    slug = user_slug(email)
    g_client, g_server = client_server_group_names(slug, name_prefix)
    pname = policy_name(slug, name_prefix)

    messages: list[str] = []

    cid = find_group_id_by_exact_name(session, base, g_client)
    if cid:
        messages.append(f"clients group exists: {g_client}")
    else:
        gid, msg = create_group(session, base, g_client, dry_run=dry_run)
        if not gid and not dry_run:
            return {"ok": False, "error": msg, "email": email}
        cid = gid
        messages.append(msg)

    sid = find_group_id_by_exact_name(session, base, g_server)
    if sid:
        messages.append(f"servers group exists: {g_server}")
    else:
        gid, msg = create_group(session, base, g_server, dry_run=dry_run)
        if not gid and not dry_run:
            return {"ok": False, "error": msg, "email": email}
        sid = gid
        messages.append(msg)

    if dry_run and (not cid or not sid):
        return {
            "ok": True,
            "dry_run": True,
            "email": email,
            "slug": slug,
            "client_group": g_client,
            "server_group": g_server,
            "client_group_id": cid,
            "server_group_id": sid,
            "messages": messages,
        }

    if not cid or not sid:
        return {"ok": False, "error": "missing group id after create", "email": email}

    if create_policy:
        ok, pmsg = ensure_pairing_policy(
            session,
            base,
            policy_name_value=pname,
            client_group_id=cid,
            server_group_id=sid,
            bidirectional=bidirectional,
            dry_run=dry_run,
        )
        messages.append(pmsg)
        if not ok:
            return {
                "ok": False,
                "error": pmsg,
                "email": email,
                "messages": messages,
            }

    if add_client_group_to_auto_groups:
        ag_raw = u.get("auto_groups") or []
        ag = [str(x) for x in ag_raw] if isinstance(ag_raw, list) else []
        if cid not in ag:
            ag.append(cid)
        role = str(u.get("role", "user"))
        is_blocked = bool(u.get("is_blocked", False))
        if dry_run:
            messages.append(f"would PUT user auto_groups (+clients): {ag}")
        else:
            pr = put_user_auto_groups(
                session,
                base,
                user_id,
                role=role,
                is_blocked=is_blocked,
                auto_groups=ag,
            )
            if response_status(pr) >= 400:
                return {
                    "ok": False,
                    "error": f"update user failed: {response_status(pr)} {pr.text[:500]}",
                    "email": email,
                    "messages": messages,
                }
            messages.append("user auto_groups updated (clients group added)")

    return {
        "ok": True,
        "email": email,
        "slug": slug,
        "user_id": user_id,
        "client_group": g_client,
        "server_group": g_server,
        "client_group_id": cid,
        "server_group_id": sid,
        "policy_name": pname if create_policy else None,
        "messages": messages,
    }


def remove_user_groups_and_policy(
    session: requests.Session,
    base: str,
    email: str,
    *,
    name_prefix: str,
    remove_policy: bool,
    strip_client_auto_group: bool,
    dry_run: bool,
) -> dict[str, Any]:
    """Remove per-user client/server groups and optional pairing policy (ensure-user-groups teardown)."""
    err = validate_email(email)
    if err:
        return {"ok": False, "error": err, "email": email}

    users = fetch_users(session, base)
    u = user_by_email(users, email)
    if not u:
        return {"ok": False, "error": "no user with this email", "email": email}

    user_id = str(u.get("id", ""))
    if not user_id:
        return {"ok": False, "error": "user has no id", "email": email}

    slug = user_slug(email)
    g_client, g_server = client_server_group_names(slug, name_prefix)
    pname = policy_name(slug, name_prefix)

    messages: list[str] = []
    cid = find_group_id_by_exact_name(session, base, g_client)
    sid = find_group_id_by_exact_name(session, base, g_server)

    if remove_policy:
        policies = fetch_policies(session, base)
        existing = next((p for p in policies if p.get("name") == pname), None)
        if existing and isinstance(existing, dict) and existing.get("id"):
            pid = str(existing["id"])
            if dry_run:
                messages.append(f"would DELETE policy {pname!r} ({pid})")
            else:
                ok, msg = delete_policy(session, base, pid)
                messages.append(msg)
                if not ok:
                    return {
                        "ok": False,
                        "error": msg,
                        "email": email,
                        "messages": messages,
                    }
        else:
            messages.append(f"policy not found (skip): {pname}")

    if strip_client_auto_group and cid:
        ag_raw = u.get("auto_groups") or []
        ag = [str(x) for x in ag_raw] if isinstance(ag_raw, list) else []
        if cid in ag:
            new_ag = [x for x in ag if x != cid]
            role = str(u.get("role", "user"))
            is_blocked = bool(u.get("is_blocked", False))
            if dry_run:
                messages.append(f"would PUT user auto_groups (remove clients group): {new_ag}")
            else:
                pr = put_user_auto_groups(
                    session,
                    base,
                    user_id,
                    role=role,
                    is_blocked=is_blocked,
                    auto_groups=new_ag,
                )
                if response_status(pr) >= 400:
                    return {
                        "ok": False,
                        "error": f"update user failed: {response_status(pr)} {pr.text[:500]}",
                        "email": email,
                        "messages": messages,
                    }
                messages.append("user auto_groups updated (clients group removed)")
        else:
            messages.append("clients group not in user auto_groups (skip)")

    for gid, gname in ((sid, g_server), (cid, g_client)):
        if not gid:
            messages.append(f"group not found (skip): {gname}")
            continue
        if dry_run:
            messages.append(f"would DELETE group {gname!r} ({gid})")
        else:
            ok, msg = delete_group(session, base, gid)
            messages.append(f"{gname}: {msg}")
            if not ok:
                return {
                    "ok": False,
                    "error": msg,
                    "email": email,
                    "messages": messages,
                }

    return {
        "ok": True,
        "email": email,
        "slug": slug,
        "user_id": user_id,
        "client_group": g_client,
        "server_group": g_server,
        "client_group_id": cid,
        "server_group_id": sid,
        "policy_name": pname if remove_policy else None,
        "messages": messages,
    }


def assign_peer_to_user_servers(
    session: requests.Session,
    base: str,
    email: str,
    *,
    name_prefix: str,
    peer_id: str | None,
    peer_name: str | None,
    remove: bool,
    dry_run: bool,
) -> dict[str, Any]:
    err = validate_email(email)
    if err:
        return {"ok": False, "error": err}

    pid, perr = resolve_peer_id(session, base, peer_id=peer_id, peer_name=peer_name)
    if perr or not pid:
        return {"ok": False, "error": perr or "missing peer id"}

    peer_id_str: str = pid

    slug = user_slug(email)
    _gc, g_server = client_server_group_names(slug, name_prefix)
    sid = find_group_id_by_exact_name(session, base, g_server)
    if not sid:
        return {
            "ok": False,
            "error": f"server group {g_server!r} does not exist; run ensure-user-groups first",
        }

    if dry_run:
        act = "remove from" if remove else "add to"
        return {
            "ok": True,
            "dry_run": True,
            "email": email,
            "peer_id": peer_id_str,
            "server_group": g_server,
            "server_group_id": sid,
            "message": f"would {act} group {g_server!r}",
        }

    g = fetch_group(session, base, sid)
    current = peer_ids_from_group_dict(g)
    resources = resources_from_group_dict(g)
    gname = str(g.get("name", g_server))

    new_peers: list[str]
    if remove:
        new_peers = [x for x in current if x != peer_id_str]
        if len(new_peers) == len(current):
            return {
                "ok": True,
                "email": email,
                "peer_id": peer_id_str,
                "server_group_id": sid,
                "message": "peer not in server group (no-op)",
            }
    else:
        new_peers = list(dict.fromkeys([*current, peer_id_str]))

    r = put_group_peers_and_resources(
        session, base, sid, name=gname, peer_ids=new_peers, resources=resources
    )
    if response_status(r) >= 400:
        return {
            "ok": False,
            "error": f"PUT group failed: {response_status(r)} {r.text[:500]}",
            "peer_id": peer_id_str,
            "server_group_id": sid,
        }

    return {
        "ok": True,
        "email": email,
        "peer_id": peer_id_str,
        "server_group": g_server,
        "server_group_id": sid,
        "message": "removed" if remove else "assigned",
    }
