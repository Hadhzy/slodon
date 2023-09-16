# pylint: disable=missing-module-docstring
# Define the API system
from __future__ import annotations

# Mainly adopted from: https://github.com/FlurryGlo/slobypy/blob/main/slobypy/rpc.py
# Further reading about this system: "miro_link_here"
import asyncio
from http import HTTPStatus
from typing import Any, Awaitable, Callable
import uuid
import json
from websockets.legacy.server import WebSocketServerProtocol
import websockets.server

import slodon.api.utils.func

# This project
from slodon.api.test.api import task1, task2
from slodon.api.utils.uri import URI
from slodon.api.utils.types import JSON, Response


__all__: tuple[str, ...] = ("RPC",)


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
        self._ws: websockets.server.WebSocketServer | None = None
        self.tasks = [task1, task2]  # represents the tasks
        asyncio.run(self.run(host, port))

    async def run(self, host: str, port: int) -> None:
        """
        Runs the websocket server

        ### Arguments
        - host (str): The host to connect to
        - port (int): The port to connect to

        ### Returns
        - None
        """
        await asyncio.gather(self.create_ws(self._handle_ws, host, port))

        pending = asyncio.all_tasks()

        self.event_loop.run_until_complete(asyncio.gather(*pending))

    # noinspection PyMethodMayBeStatic
    def serve_content(self, uri: URI) -> JSON:
        """
        Runs the websocket server

        ### Arguments
        - host (str): The host to connect to
        - port (int): The port to connect to

        ### Returns
        - None
        """
        _language = uri.uri.split("/")[1]  # get the language
        slodon.api.utils.func.LANGUAGE = _language  # set the language

        from slodon.api.utils.static import (
            RESPONSES,
        )  # pylint: disable=import-outside-toplevel

        return json.dumps(RESPONSES.get(uri.formate()))

    async def _handle_ws(self, conn: WebSocketServerProtocol, path: str) -> None:
        """
        Handles the websocket connection and sends a response to the client

        ### Arguments
        - conn (WebsocketServerProtocol): The websocket connection
        - path (str): corresponding uri(endpoint)

        ### Returns
            - None
        """
        _uri = URI(path)  # make a wrapper around the path
        content = self.serve_content(_uri)  # get the content
        status = (
            HTTPStatus.OK if content != "null" else HTTPStatus.NOT_FOUND
        )  # set the status to OK

        response: Response = {
            "status": status,  # http status code
            "message": status.phrase,  # http status message
            "content": content,  # actual content
        }

        await conn.send(json.dumps(response))  # send the response to the client

    async def create_ws(
        self, ws_handler: [Callable, Awaitable[Any]], host: str, port: int # type: ignore[valid-type]
    ) -> None:
        """
        Creates a websocket connection to the React frontend

        ### Arguments
        - ws_handler (callable): The function to handle the websocket connection
        - host (str): The host to connect to
        - port (int): The port to connect to

        ### Returns
        - None
        """

        self._ws = await websockets.server.serve(ws_handler, host, port)
        await self._ws.serve_forever()


class Event:  # pylint: disable=too-few-public-methods
    """
    Represents an event coming from the client(model)
    """


if __name__ == "__main__":
    RPC()
