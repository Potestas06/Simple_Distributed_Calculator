import asyncio
import websockets

# sents the message to the spooler
async def redirect(message):
    async with websockets.connect(f"ws://localhost:8001") as websocket: # type: ignore
        await websocket.send(message)
        print(f"Sent: {message}")

        response = await websocket.recv()
        print(f"Result: {response}")
        return response

# handels incoming request
async def handler(websocket, path):
    async for message in websocket:
        print(f"Received message: {message}")
        reply = await redirect(message)
        await websocket.send(reply)
        print(f"Sent reply: {reply}")

start_server = websockets.serve(handler, "localhost", 8000) # type: ignore

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
