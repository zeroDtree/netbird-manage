"""Shared NetBird Management API HTTP helpers."""

from __future__ import annotations

import time
from typing import Any

import requests


def api_url(base: str, path: str) -> str:
    return f"{base.rstrip('/')}{path}"


def response_status(response: requests.Response) -> int:
    code = response.status_code
    return 0 if code is None else code


def request_with_retry(
    session: requests.Session,
    method: str,
    url: str,
    *,
    headers: dict[str, str] | None = None,
    json_body: Any = None,
    max_retries: int = 4,
    timeout: float = 60.0,
) -> requests.Response:
    delay = 1.0
    last_exc: Exception | None = None
    for attempt in range(max_retries):
        try:
            r = session.request(
                method,
                url,
                headers=headers,
                json=json_body,
                timeout=timeout,
            )
            code = response_status(r)
            if code == 429 or (500 <= code < 600):
                if attempt < max_retries - 1:
                    time.sleep(delay)
                    delay = min(delay * 2, 30.0)
                    continue
            return r
        except requests.RequestException as e:
            last_exc = e
            if attempt < max_retries - 1:
                time.sleep(delay)
                delay = min(delay * 2, 30.0)
                continue
            raise
    if last_exc:
        raise last_exc
    raise RuntimeError("request_with_retry: unreachable")


def session_with_token(token: str) -> requests.Session:
    s = requests.Session()
    s.headers["Authorization"] = f"Token {token}"
    return s


def json_headers() -> dict[str, str]:
    """Standard JSON Accept + Content-Type headers for NetBird REST bodies."""
    return {"Accept": "application/json", "Content-Type": "application/json"}
