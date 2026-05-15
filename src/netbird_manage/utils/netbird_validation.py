"""Shared validation helpers for NetBird tooling."""

from __future__ import annotations

import re

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def validate_email(email: str) -> str | None:
    if not email or not EMAIL_RE.match(email.strip()):
        return "invalid email"
    return None
