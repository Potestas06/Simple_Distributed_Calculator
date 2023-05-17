import asyncio
import websockets
import json
import datetime
import os

LOGFILE_PATH = "logs/logfile.log"


async def log(message, response, checksum):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    response = json.dumps({"result": response})
    checksum = json.dumps({"checksum": checksum})
    log_entry_message = f"[{current_time}] {message}"
    if not os.path.exists(LOGFILE_PATH):
        with open(LOGFILE_PATH, "w"):
            pass
    with open(LOGFILE_PATH, "a") as logfile:
        logfile.write(f"{log_entry_message}")
        logfile.write(f"{response}")
        logfile.write(f"{checksum}\n")


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

start_server = websockets.serve(handler, "localhost", 8010)  # type: ignore

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
