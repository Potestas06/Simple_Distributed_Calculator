import asyncio
import websockets


async def redirect(message):
    async with websockets.connect(f"ws://localhost:8001") as websocket:
        await websocket.send(message)
        print(f"Sent: {message}")

        response = await websocket.recv()
        print(f"Result: {response}")
        return response


async def handler(websocket, path):
    async for message in websocket:
        print(f"Received message: {message}")
        reply = await redirect(message)
        await websocket.send(reply)
        print(f"Sent reply: {reply}")

start_server = websockets.serve(handler, "localhost", 8000)
