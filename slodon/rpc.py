from __future__ import annotations
# Define the API system

# Mainly adopted from: https://github.com/FlurryGlo/slobypy/blob/main/slobypy/rpc.py

import asyncio
from typing import Any, Awaitable, Callable, Coroutine

import websockets.exceptions

from websockets.legacy.server import WebSocketServerProtocol
from websockets.server import WebSocketServer, serve

# This project
from slodon.test.api import task1, task2
__all__: tuple[str, ...] = (
    "RPC",
)


class RPC:
    CURRENT_VERSION = "0.A1"

    def __init__(self, host: str = "localhost", port: int = 8765) -> None:
        self.event_loop = asyncio.get_event_loop()  # get the event loop
        asyncio.set_event_loop(self.event_loop)  # set the event loop

        self.ws: WebSocketServer | None = None
        self.tasks = [task1, task2]  # represents the tasks
        asyncio.run(self.run(host, port))

    async def run(self, host: str, port: int):

        await asyncio.gather(
           task1(), self.create_ws(self._handle_ws, host, port)
        )

        pending = asyncio.all_tasks()
        self.event_loop.run_until_complete(asyncio.gather(*pending))

    async def _handle_ws(self, conn: WebSocketServerProtocol) -> None:
        """
        Used to handle messages from the websocket connection(client)
        :param conn:
        :return: NOne
        """

    async def create_ws(self, ws_handler: [[Callable], Awaitable[Any]], host: str, port: int) -> None:
        """
        Creates a websocket connection to the React frontend

        ### Arguments
        - ws_handler (callable): The function to handle the websocket connection
        - host (str): The host to connect to
        - port (int): The port to connect to

        ### Returns
        - None

        :param ws_handler:
        :param host:
        :param port:
        :return:
        """

        self.ws = await serve(ws_handler, host, port)
        await self.ws.serve_forever()


if __name__ == '__main__':
    RPC()




