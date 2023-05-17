import asyncio
import json
import websockets
import random

ports = [8200, 8201, 8202, 8203, 8204]

# gets the checksum from a random port
async def get_checksum(message):
    return await connect(random.choice(ports), message)


# checks if the checksum is correct
async def checker(result, message):
    if result == await get_checksum(message):
        return True
    else:
        return False

# logs the message, response, and checksum
async def log(message, response, checksum):
    async with websockets.connect("ws://localhost:8010") as websocket: # type: ignore
        await websocket.send(json.dumps({
            "checksum": checksum,
            "message": message,
            "response": response
        }))
        print(f'Sent "{message}" to logger')

        reply = await websocket.recv()
        data = json.loads(reply)
        if data["status"] == "success":
            print(f"Logged: {message}")
        else:
            print(f"Failed to log: {message}")


# connects to a port and sends a message
async def connect(port, message):
    async with websockets.connect(f"ws://localhost:{port}") as websocket: # type: ignore
        await websocket.send(message)
        print(f"Sent: {message}")

        response = await websocket.recv()
        print(f"Result: {response}")
        return response


# handles incoming request
async def handler(websocket, path):
    async for message in websocket:
        print(f"Received message: {message}")
        reply = await get_checksum(message)
        await log(message, reply, await checker(reply, message))
        await websocket.send(reply)
        print(f"Sent reply: {reply}")


start_server = websockets.serve(handler, "localhost", 8001) # type: ignore

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
