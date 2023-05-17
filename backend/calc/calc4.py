import asyncio
import websockets
import json


async def calc(message):
    try:
        data = json.loads(message)
        work = data['work']
        if not isinstance(work, str):
            raise NameError("Invalid input")
        result = str(eval(work))
        with open('calculations.json', 'r') as f:
            for line in f:
                if json.loads(line)['work'] == work:
                    return result
        with open('calculations.json', 'a') as f:
            f.write(json.dumps({'work': work, 'result': result}) + '\n')
        return result
    except (NameError, KeyError, TypeError, SyntaxError) as e:
        error_msg = "Error: " + str(e)
        return error_msg
    except Exception as e:
        error_msg = "Unknown error: " + str(e)
        return error_msg


async def handler(websocket, path):
    try:
        async for message in websocket:
            print(f"Received message: {message}")
            reply = await calc(message)
            await websocket.send(reply)
            print(f"Sent reply: {reply}")
    except websockets.exceptions.ConnectionClosed:
        print("Connection closed")

start_server = websockets.serve(handler, "localhost", 8203)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
