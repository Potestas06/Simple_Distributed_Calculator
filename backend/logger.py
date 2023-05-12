import asyncio
import websockets
import json
import datetime

LOGFILE_PATH = "logfile.log"

async def log(message, reply):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry_message = f"[{current_time}] {message}"
    log_entry_reply = f"[{current_time}] {reply}"
    with open(LOGFILE_PATH, "a") as logfile:
        logfile.write(f"{log_entry_message}\n")
        logfile.write(f"{log_entry_reply}\n")

async def handler(websocket, path):
    async for message in websocket:
        print(f"Received message: {message}")
        await log(message, reply)
        reply = json.dumps({"status": "success"})
        await websocket.send(reply)
        print(f"Sent reply: {reply}")

start_server = websockets.serve(handler, "localhost", 8010)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
