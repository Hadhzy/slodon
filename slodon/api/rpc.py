from __future__ import annotations
# Define the API system

# Mainly adopted from: https://github.com/FlurryGlo/slobypy/blob/main/slobypy/rpc.py
# Further reading about this system: "miro_link_here"
import asyncio
from typing import Any, Awaitable, Callable
import uuid
import json
from websockets.legacy.server import WebSocketServerProtocol
import websockets.server

# This project
from slodon.api.test.api import task1, task2
from slodon.api.utils.uri import URI
from slodon.api.utils.types import JSON
from slodon.api.utils.static import RESPONSES

__all__: tuple[str, ...] = (
    "RPC",
)


class RPC:
    """
    Websocket server
    """
    CURRENT_VERSION = "0.A1"

    def __init__(self, host: str = "localhost", port: int = 8765) -> None:
        """
        Websocket initialization

        ### Arguments
        - host (str): The host to connect to
        - port (int): The port to connect to

        ### Returns
        - None
        """
        self._id = uuid.uuid4()  # generate a random id

        self.event_loop = asyncio.get_event_loop()  # get the event loop
        asyncio.set_event_loop(self.event_loop)  # set the event loop
        self.ws: websockets.server.WebSocketServer | None = None
        self.tasks = [task1, task2]  # represents the tasks
        print("here1")
        asyncio.run(self.run(host, port))

    async def run(self, host: str, port: int):

        await asyncio.gather(
            task1(), self.create_ws(self._handle_ws, host, port)
        )

        pending = asyncio.all_tasks()

        self.event_loop.run_until_complete(asyncio.gather(*pending))

    # noinspection PyMethodMayBeStatic
    def serve_content(self, uri) -> JSON:
        return json.dumps(RESPONSES.get(uri))

    async def _handle_ws(self, conn: WebSocketServerProtocol, path: str) -> None:
        """
        Handles the websocket connection and sends a response to the client

        ### Arguments
        - conn (WebsocketServerProtocol): The websocket connection
        - path (str): corresponding uri(endpoint)


        ### Returns
            - None
        """
        _uri = URI(path).uri  # make a wrapper around the path
        await conn.send(self.serve_content(_uri))  # send something back to the client based on the endpoint(_uri)

    async def create_ws(self, ws_handler: [[Callable], Awaitable[Any]], host: str, port: int) -> None:
        """
        Creates a websocket connection to the React frontend

        ### Arguments
        - ws_handler (callable): The function to handle the websocket connection
        - host (str): The host to connect to
        - port (int): The port to connect to

        ### Returns
        - None
        """

        self.ws = await websockets.server.serve(ws_handler, host, port)
        await self.ws.serve_forever()


if __name__ == '__main__':
    RPC()


class Event:
    pass
