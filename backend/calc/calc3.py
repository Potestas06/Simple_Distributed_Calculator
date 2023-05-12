import asyncio
import websockets
import json


async def calc(message):
    try:
        data = json.loads(message)
        work = data['work']
        if not isinstance(work, str):
            raise ValueError("Invalid input")
        return str(eval(work))
    except (ValueError, KeyError, TypeError, SyntaxError):
        return "Error: Invalid input"


async def handler(websocket, path):
    async for message in websocket:
        print(f"Received message: {message}")
        reply = await calc(message)
        await websocket.send(reply)
        print(f"Sent reply: {reply}")

start_server = websockets.serve(handler, "localhost", 8202)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
