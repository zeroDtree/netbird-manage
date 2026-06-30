"""Shared CLI argument definitions for NetBird Management API tools."""

from __future__ import annotations

import argparse
import os

DEFAULT_API_BASE = "https://api.netbird.io"


def load_netbird_env() -> None:
    """Load NETBIRD_* from .env and .env.secrets in the current working directory."""
    from dotenv import load_dotenv

    load_dotenv(".env")
    load_dotenv(".env.secrets")


def netbird_connection_parent_parser() -> argparse.ArgumentParser:
    """Return a parent parser with common NetBird connection flags (add_help=False)."""
    p = argparse.ArgumentParser(add_help=False)
    p.add_argument(
        "--base-url",
        default=os.environ.get("NETBIRD_API_BASE", DEFAULT_API_BASE),
        help=(
            f"Management API base URL (default: env NETBIRD_API_BASE / .env, or "
            f"{DEFAULT_API_BASE})"
        ),
    )
    p.add_argument(
        "--token",
        default=os.environ.get("NETBIRD_TOKEN", ""),
        help="Personal access token (default: NETBIRD_TOKEN / .env)",
    )
    p.add_argument(
        "--dry-run",
        action="store_true",
        help=(
            "Skip mutating NetBird Management API calls when the command supports it "
            "(may still GET for validation)."
        ),
    )
    return p
