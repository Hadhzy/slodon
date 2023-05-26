#!/usr/bin/env python
# Test client
import asyncio
import websockets

uri_ = "/test1"


async def hello():
    uri = "ws://localhost:8765" + uri_
    async with websockets.connect(uri) as websocket:
        name = input("What's your name? ")

        await websocket.send(name)
        print(f">>> {name}")

        greeting = await websocket.recv()
        print(f"<<< {greeting}")

if __name__ == "__main__":
    asyncio.run(hello())


