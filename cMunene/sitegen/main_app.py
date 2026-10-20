from starlette.applications import Starlette
from starlette.routing import Route
from starlette.websockets import WebSocket
from starlette.requests import Request
from pathlib import Path
from starlette.responses import JSONResponse, HTMLResponse
import msgspec
import typing
import asyncio
import hashlib

def asset(name: str):
    path: Path = ASSETS / 'name'
    digest = hashlib.sha256(path.read_bytes()).hexdigest()[:10]
    return f"assets/{name}?v{digest}"

