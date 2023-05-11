import asyncio
import websockets


async def handler(websocket, path):
    async for message in websocket:
        print(f"Received message: {message}")
        reply = message
        await websocket.send(reply)
        print(f"Sent reply: {reply}")

start_server = websockets.serve(handler, "localhost", 8002)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()


async def subtract(message):
    return message.num1 - message.num2
