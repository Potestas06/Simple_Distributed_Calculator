import asyncio
import websockets
import json
import datetime
import os

LOGFILE_PATH = "logs\logfile.log"


async def log(message, response, checksum):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry_message = f"[{current_time}] {message}"
    log_entry_response = f"[{current_time}] {response}"
    log_entry_checksum = f"[{current_time}] {'Checksum is' + checksum}"
    if not os.path.exists(LOGFILE_PATH):
        with open(LOGFILE_PATH, "w"):
            pass  # Create the file if it doesn't exist
    with open(LOGFILE_PATH, "a") as logfile:
        logfile.write(f"{log_entry_message}\n")
        logfile.write(f"{log_entry_response}\n")
        logfile.write(f"{log_entry_checksum}\n")


async def get_reply(websocket):
    async for response in websocket:
        return response


async def get_checksum(websocket):
    async for checksum in websocket:
        return checksum


async def handler(websocket, path):
    response = await get_reply(websocket)
    checksum = await get_checksum(websocket)
    async for message in websocket:
        print(f"Received message: {message}")
        await log(message, response, checksum)
        reply = json.dumps({"status": "success"})
        await websocket.send(reply)
        print(f"Sent reply: {reply}")

start_server = websockets.serve(handler, "localhost", 8010)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
