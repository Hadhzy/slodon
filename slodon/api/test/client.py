#!/usr/bin/env python
# Test client
import asyncio
import websockets


async def hello():
    uri = "ws://localhost:8765/en/test1"
    async with websockets.connect(uri) as websocket:
        greeting = await websocket.recv()
        print(f"<<< {greeting}")


if __name__ == "__main__":
    asyncio.run(hello())
