from __future__ import annotations
# Define the API system

# Mainly adopted from: https://github.com/FlurryGlo/slobypy/blob/main/slobypy/rpc.py

import asyncio
import json
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass

from datetime import datetime
from pathlib import Path
from typing import TYPE_CHECKING, Any, Awaitable, Callable, Coroutine

import websockets.exceptions

from websockets.legacy.server import WebSocketServerProtocol
from websockets.server import WebSocketServer, serve

__all__: tuple[str, ...] = (
    "RPC",
)


class RPC:
    CURRENT_VERSION = "0.A1"

