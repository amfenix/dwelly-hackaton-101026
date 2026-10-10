"""The live desk (flowkit/live/server.py) as one Vercel Python function, behind a shared password.

Every path is rewritten here (vercel.json). The keys and DESK_PASSWORD come from the project's
environment; with DESK_PASSWORD set, every request needs HTTP Basic auth (any user name).
"""

from __future__ import annotations

import base64
import hmac
import os
import sys
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlsplit

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "flowkit" / "live"))

import server  # noqa: E402  (flowkit/live/server.py)

os.chdir(ROOT)
server.Handler.desk = server.Desk.load()
server.Handler.pace = 0.1


def _allowed(header: str | None) -> bool:
    password = os.environ.get("DESK_PASSWORD")
    if not password:
        return True
    if not header or not header.startswith("Basic "):
        return False
    try:
        given = base64.b64decode(header[6:]).decode("utf-8").partition(":")[2]
    except ValueError:
        return False
    return hmac.compare_digest(given.encode(), password.encode())


def _original(path: str) -> str:
    """The path the browser asked for: the rewrite (vercel.json) sends it as `__path`."""
    url = urlsplit(path)
    query = parse_qsl(url.query, keep_blank_values=True)
    original = next((v for k, v in query if k == "__path"), None)
    if original is None:
        return path
    rest = urlencode([(k, v) for k, v in query if k != "__path"])
    return original + (f"?{rest}" if rest else "")


class handler(server.Handler):  # the name Vercel looks for
    def _gate(self) -> bool:
        self.path = _original(self.path)
        if _allowed(self.headers.get("Authorization")):
            return True
        self.send_response(401)
        self.send_header("WWW-Authenticate", 'Basic realm="desk", charset="UTF-8"')
        self.send_header("Content-Length", "0")
        self.end_headers()
        return False

    def do_GET(self) -> None:
        if self._gate():
            super().do_GET()

    def do_POST(self) -> None:
        if self._gate():
            super().do_POST()
