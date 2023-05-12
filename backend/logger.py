import asyncio
import websockets
import json
import datetime
import os

LOGFILE_PATH = "logfile.log"


async def log(message, response, checksum):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    response = json.dumps({"result": response})
    checksum = json.dumps({"checksum": checksum})
    log_entry_message = f"[{current_time}] {message}"
    log_entry_response = f"[{current_time}] {response}"
    log_entry_checksum = f"[{current_time}] {checksum}"
    if not os.path.exists(LOGFILE_PATH):
        with open(LOGFILE_PATH, "w"):
            pass  # Create the file if it doesn't exist
    with open(LOGFILE_PATH, "a") as logfile:
        logfile.write(f"{log_entry_message}\n")
        logfile.write(f"{log_entry_response}\n")
        logfile.write(f"{log_entry_checksum}\n\n")

async def handler(websocket, path):
    async for message in websocket:
        data = json.loads(message)
        checksum = data.get("checksum")
        message = data.get("message")
        response = data.get("response")
        print(f"Received message: {message}")
        print(f"Received response: {response}")
        print(f"Received checksum: {checksum}")
        await log(message, response, checksum)
        reply = json.dumps({"status": "success"})
        await websocket.send(reply)
        print(f"Sent reply: {reply}")

start_server = websockets.serve(handler, "localhost", 8010)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
