import asyncio
import websockets
import json


async def subtract(message):
    data = json.loads(message)
    num1 = int(data["num1"])
    num2 = int(data["num2"])
    result = num1 - num2
    return str(result)


async def handler(websocket, path):
    async for message in websocket:
        print(f"Received message: {message}")
        reply = await subtract(message)
        await websocket.send(str(reply))
        print(f"Sent reply: {reply}")

start_server = websockets.serve(handler, "localhost", 8002)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
