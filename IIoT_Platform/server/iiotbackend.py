import asyncio
import websockets
import json as jsn
import time as tm
import configparser
import traceback
import logging as lg
import logging.handlers as handlers
from controller.protocontroller import *


########################################################
# Read configuration parameters for web  socket server #
########################################################
config = configparser.ConfigParser()
config.read('config.properties')
h_params = config['websocket.server']
f_params = config['websocket.logs']

logger = lg.getLogger('IIot platform')
logger.setLevel(lg.INFO)

formatter = lg.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

loghandler = handlers.RotatingFileHandler('trace.log', maxBytes=20000000, backupCount=10)
loghandler.setLevel(lg.INFO)
loghandler.setFormatter(formatter)

errorhandler = handlers.RotatingFileHandler('error.log', maxBytes=20000000, backupCount=10)
errorhandler.setLevel(lg.ERROR)
errorhandler.setFormatter(formatter)

logger.addHandler(loghandler)
logger.addHandler(errorhandler)


async def get_devices():
    res = getDevices()
    return res

async def get_device_data(devdatareq):
    euiList = devdatareq.devEuiList
    tmpstr =', '.join(["'"+val+"'" for val in euiList])
    res = getDeviceData(tmpstr)
    return res


async def producer(message):
    try:
        req = Request()
        req.ParseFromString(message)

        if req.type == 'get_devices':
            return await get_devices()

        elif req.type == 'get_device_data':
            return await get_device_data(req.devicedata)
        '''
        elif func_name == 'get_device_history':
            return await get_device_history(json_object['devEui'], json_object['utc_timestamp'], ws)
        else:
            return "Bad function name" '''
    except Exception as ex:
        logger.error(ex)
        traceback.print_exc()
        return 'Bad message format'


async def echo(ws, path):
    logger.info('Start back-end server')
    async for message in ws:
        logger.info('Incoming message <======' + str(message))
        prod_mess = await producer(message)
        logger.info('Outgoing message =======>' + str(prod_mess))
        await ws.send(prod_mess)


start_server = websockets.serve(echo, h_params['host'], h_params['port'])
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
