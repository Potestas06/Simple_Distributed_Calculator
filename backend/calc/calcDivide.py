import asyncio
import websockets
import json


async def multiply(message):
    data = json.loads(message)
    num1 = int(data['num1'])
    num2 = int(data['num2'])
    if num2 == 0:
        result = "Error division by 0!"
    else:
        result = num1 / num2
    return str(result)


async def handler(websocket, path):
    async for message in websocket:
        print(f"Received message: {message}")
        reply = await multiply(message)
        await websocket.send(reply)
        print(f"Sent reply: {reply}")

start_server = websockets.serve(handler, "localhost", 8103)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
