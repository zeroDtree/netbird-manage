#!/usr/bin/env python3
"""
NetBird machine assignment: per-user client/server groups, pairing policy, and peer grants.

Subcommands:
  ensure-user-groups — create ``{prefix}{slug}-clients`` / ``...-servers`` groups; optional policy + user auto_groups.
  remove-user-groups — delete those groups and pairing policy; optional strip clients group from user auto_groups.
  manage-server-peer — add or remove a peer from the user's servers group (GET/merge/PUT /api/groups).

Environment: NETBIRD_API_BASE, NETBIRD_TOKEN (or --token). Loads ``.env`` and ``.env.secrets`` from the current working directory.

Run: uv run policy-manage ensure-user-groups --email user@example.com --dry-run
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time

from ..services.assign_core import (
    assign_peer_to_user_servers,
    ensure_user_groups_and_policy,
    remove_user_groups_and_policy,
)
from ..utils.cli import load_netbird_env, netbird_connection_parent_parser
from ..utils.client import session_with_token


def _parent_parser() -> argparse.ArgumentParser:
    return netbird_connection_parent_parser()


def _emails_from_args(
    emails: list[str], file_path: str | None
) -> tuple[list[str], str | None]:
    if file_path:
        try:
            from .user_manage import load_rows
        except ImportError:
            return [], "internal error: could not import load_rows"
        try:
            rows = load_rows(file_path)
        except Exception as e:
            return [], f"failed to read file: {e}"
        out: list[str] = []
        for row in rows:
            e = (row.get("email") or "").strip()
            if e:
                out.append(e)
        if not out:
            return [], "no email column values in file"
        return out, None
    if emails:
        return list(emails), None
    return [], "pass --email one or more times or use --file"


def run_ensure(args: argparse.Namespace) -> int:
    emails, err = _emails_from_args(args.email, args.file)
    if err:
        print(err, file=sys.stderr)
        return 2
    if not args.token:
        print("Missing PAT: set NETBIRD_TOKEN or pass --token", file=sys.stderr)
        return 4

    session = session_with_token(args.token)
    failed = 0
    for i, email in enumerate(emails):
        res = ensure_user_groups_and_policy(
            session,
            args.base_url,
            email,
            name_prefix=args.name_prefix,
            create_policy=args.create_policy,
            bidirectional=args.bidirectional,
            add_client_group_to_auto_groups=args.add_client_group_to_auto_groups,
            dry_run=args.dry_run,
        )
        if not res.get("ok"):
            failed += 1
            print(f"{email}: {res.get('error')}", file=sys.stderr)
        else:
            print(json.dumps(res, indent=2))
        if i < len(emails) - 1:
            time.sleep(args.delay_between_rows)
    return 1 if failed else 0


def run_remove(args: argparse.Namespace) -> int:
    emails, err = _emails_from_args(args.email, args.file)
    if err:
        print(err, file=sys.stderr)
        return 2
    if not args.token:
        print("Missing PAT: set NETBIRD_TOKEN or pass --token", file=sys.stderr)
        return 4
    if not args.dry_run and not args.yes:
        print("Refusing to delete without --yes (or use --dry-run).", file=sys.stderr)
        return 5

    session = session_with_token(args.token)
    failed = 0
    for i, email in enumerate(emails):
        res = remove_user_groups_and_policy(
            session,
            args.base_url,
            email,
            name_prefix=args.name_prefix,
            remove_policy=not args.skip_policy_delete,
            strip_client_auto_group=not args.keep_client_in_auto_groups,
            dry_run=args.dry_run,
        )
        if not res.get("ok"):
            failed += 1
            print(f"{email}: {res.get('error')}", file=sys.stderr)
        else:
            print(json.dumps(res, indent=2))
        if i < len(emails) - 1:
            time.sleep(args.delay_between_rows)
    return 1 if failed else 0


def run_manage_server_peer(args: argparse.Namespace) -> int:
    if not args.token:
        print("Missing PAT: set NETBIRD_TOKEN or pass --token", file=sys.stderr)
        return 4
    if not args.peer_id and not args.peer_name:
        print("Provide --peer-id and/or --peer-name", file=sys.stderr)
        return 2

    session = session_with_token(args.token)
    res = assign_peer_to_user_servers(
        session,
        args.base_url,
        args.email,
        name_prefix=args.name_prefix,
        peer_id=args.peer_id or None,
        peer_name=args.peer_name or None,
        remove=args.remove,
        dry_run=args.dry_run,
    )
    print(json.dumps(res, indent=2))
    return 0 if res.get("ok") else 1


def run(argv: list[str] | None = None) -> int:
    load_netbird_env()
    parent = _parent_parser()
    main = argparse.ArgumentParser(
        description="NetBird per-user groups and machine assignment CLI.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = main.add_subparsers(dest="command", required=True)

    p_ensure = sub.add_parser(
        "ensure-user-groups",
        parents=[parent],
        help="Create client/server groups (and optional policy / auto_groups)",
    )
    p_ensure.add_argument(
        "--email",
        action="append",
        default=[],
        metavar="ADDR",
        help="User email (repeat for multiple)",
    )
    p_ensure.add_argument(
        "--file",
        "-f",
        default=None,
        help="CSV or Excel with an email column",
    )
    p_ensure.add_argument(
        "--name-prefix",
        default=os.environ.get("NETBIRD_ASSIGN_NAME_PREFIX", "nb"),
        help="Group/policy name prefix (default: nb → nb-{slug}-clients)",
    )
    p_ensure.add_argument(
        "--create-policy",
        action="store_true",
        help="Create pairing policy (clients → servers) if missing",
    )
    p_ensure.add_argument(
        "--bidirectional",
        action="store_true",
        help="With --create-policy, set bidirectional rule",
    )
    p_ensure.add_argument(
        "--add-client-group-to-auto-groups",
        action="store_true",
        help="PUT user to append clients group to auto_groups",
    )
    p_ensure.add_argument(
        "--delay-between-rows",
        type=float,
        default=0.35,
        metavar="SECONDS",
        help=(
            "Pause after each row's NetBird calls before processing the next email "
            "from `--file`."
        ),
    )

    p_remove = sub.add_parser(
        "remove-user-groups",
        parents=[parent],
        help="Delete per-user client/server groups and pairing policy",
    )
    p_remove.add_argument(
        "--email",
        action="append",
        default=[],
        metavar="ADDR",
        help="User email (repeat for multiple)",
    )
    p_remove.add_argument(
        "--file",
        "-f",
        default=None,
        help="CSV or Excel with an email column",
    )
    p_remove.add_argument(
        "--name-prefix",
        default=os.environ.get("NETBIRD_ASSIGN_NAME_PREFIX", "nb"),
        help="Same prefix as ensure-user-groups (default: nb)",
    )
    p_remove.add_argument(
        "--skip-policy-delete",
        action="store_true",
        help="Do not DELETE the pairing policy",
    )
    p_remove.add_argument(
        "--keep-client-in-auto-groups",
        action="store_true",
        help="Do not remove clients group id from user auto_groups",
    )
    p_remove.add_argument(
        "--yes",
        action="store_true",
        help="Required for real deletes (omit with --dry-run only)",
    )
    p_remove.add_argument(
        "--delay-between-rows",
        type=float,
        default=0.35,
        metavar="SECONDS",
        help=(
            "Pause after each row's NetBird calls before processing the next email "
            "from `--file`."
        ),
    )

    p_manage = sub.add_parser(
        "manage-server-peer",
        parents=[parent],
        help="Add or remove a machine (peer) in the user's servers group",
    )
    p_manage.add_argument("--email", required=True, help="Target user email")
    p_manage.add_argument("--peer-id", default="", help="NetBird peer id")
    p_manage.add_argument("--peer-name", default="", help="Peer hostname (exact match)")
    p_manage.add_argument(
        "--remove",
        action="store_true",
        help="Remove peer from the user's servers group",
    )
    p_manage.add_argument(
        "--name-prefix",
        default=os.environ.get("NETBIRD_ASSIGN_NAME_PREFIX", "nb"),
        help="Same prefix as ensure-user-groups (default: nb)",
    )

    args = main.parse_args(list(sys.argv[1:] if argv is None else argv))
    if args.command == "ensure-user-groups":
        return run_ensure(args)
    if args.command == "remove-user-groups":
        return run_remove(args)
    if args.command == "manage-server-peer":
        return run_manage_server_peer(args)
    raise RuntimeError(f"unknown command: {args.command}")


def main() -> None:
    raise SystemExit(run())


if __name__ == "__main__":
    main()
