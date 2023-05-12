import asyncio
import websockets
import json


async def add(message):
    data = json.loads(message)
    num1 = int(data['num1'])
    num2 = int(data['num2'])
    result = num1 + num2
    return str(result)


async def handler(websocket, path):
    async for message in websocket:
        print(f"Received message: {message}")
        reply = await add(message)
        await websocket.send(reply)
        print(f"Sent reply: {reply}")

start_server = websockets.serve(handler, "localhost", 8100)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
