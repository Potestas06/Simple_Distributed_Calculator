import asyncio
import websockets


async def handler(websocket, path):
    async for message in websocket:
        print(f"Received message: {message}")
        reply = Add(message)
        await websocket.send(reply)
        print(f"Sent reply: {reply}")


async def Add(message):
    return (message.num1 + message.num2)



start_server = websockets.serve(handler, "localhost", 8001)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
