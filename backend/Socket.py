import asyncio
import websockets


async def connect(port, message):
    async with websockets.connect("ws://localhost:" + port) as websocket:
        await websocket.send(message)
        print(f"Sent: {message}")

        response = await websocket.recv()
        print(f"Result: {response}")
        return response


async def add(message):
    return await connect("8001", message)

async def subtract(message):
    return await connect("8002", message)


async def handler(websocket, path):
    async for message in websocket:
        print(f"Received message: {message}")
        reply = await add(message)
        await websocket.send(reply)
        print(f"Sent reply: {reply}")

start_server = websockets.serve(handler, "localhost", 8000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
