import asyncio
import websockets
import json
import datetime
import os

LOGFILE_PATH = "logfile.log"

async def log(message):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{current_time}] {message}"
    if not os.path.exists(LOGFILE_PATH):
        with open(LOGFILE_PATH, "w"):
            pass  # Erstelle die Datei, falls sie nicht existiert
    with open(LOGFILE_PATH, "a") as logfile:
        logfile.write(f"{log_entry}\n")

async def handler(websocket, path):
    async for message in websocket:
        print(f"Received message: {message}")
        await log(message)
        reply = json.dumps({"status": "success"})
        await websocket.send(reply)
        print(f"Sent reply: {reply}")

start_server = websockets.serve(handler, "localhost", 8010)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
