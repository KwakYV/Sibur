import asyncio
import websockets
import json as jsn
# import time as tm
import configparser
import traceback


config = configparser.ConfigParser()
config.read('config.properties')
v_params = config['config.vega']
h_params = config['websocket.server']


async def echo(ws, path):
    async for message in ws:
        print(message)
        #prod_mess = await producer(message, v_params)
        str = 'helo'

        for i in range(2):
            await ws.send("For " + str(i))
start_server = websockets.serve(echo, h_params['host'], h_params['port'])
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()