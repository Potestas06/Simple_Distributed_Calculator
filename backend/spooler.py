import asyncio
import json
import websockets


async def connect(port, message):
    async with websockets.connect(f"ws://localhost:{port}") as websocket:
        await websocket.send(message)
        print(f"Sent: {message}")

        response = await websocket.recv()
        print(f"Result: {response}")
        return response


async def add(message):
    return await connect("8100", message)


async def subtract(message):
    return await connect("8101", message)


async def multiply(message):
    return await connect("8102", message)


async def divide(message):
    return await connect("8103", message)


async def handler(websocket, path):
    async for message in websocket:
        print(f"Received message: {message}")
        data = json.loads(message)

        method = data.get("method")
        if method == "add":
            reply = await add(message)
        elif method == "subtract":
            reply = await subtract(message)
        elif method == "multiply":
            reply = await multiply(message)
        elif method == "divide":
            reply = await divide(message)
        else:
            reply = "Invalid method"

        await websocket.send(reply)
        print(f"Sent reply: {reply}")


start_server = websockets.serve(handler, "localhost", 8001)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
