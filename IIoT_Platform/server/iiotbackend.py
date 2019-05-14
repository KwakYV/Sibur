import asyncio
import websockets
import configparser
import traceback
import logging as lg
import logging.handlers as handlers
from controller.protocontroller import *
from protos.iiot_pb2 import *
from integration.brocaar.lora_app_server.connection import *
from tests.api_grpc import *

#TODO - Move config reading and logger initialization from here to package controller __init__.py
########################################################
# Read configuration parameters for web  socket server #
########################################################
config = configparser.ConfigParser()
config.read('../configs/server.properties')
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


async def get_devices_func():
    res = get_devices()
    return res


async def get_device_data_func(devdatareq):
    euilist = devdatareq.devEuiList
    tmpstr = ', '.join(["'"+val+"'" for val in euilist])
    res = get_device_data(tmpstr)
    return res


async def get_device_history_func(historyreq):
    euilist = historyreq.devEuiList
    tmpstr = ', '.join(["'" + val + "'" for val in euilist])
    ts = historyreq.ts
    res = get_device_data_history(tmpstr, ts)
    return res


async def get_dev_prof_id():
    res = getDeviceProfileID()
    return res


async def get_apps():
    res = getApps()
    return res


async def create_device_request(create_request):
    try:
        create_device_func(create_request)
    except Exception as ex:
        raise ex
    return 'Device created'


async def get_device_type_list():
    try:
        return get_device_types()
    except Exception as ex:
        raise ex


async def get_plant_list():
    try:
        return get_plants()
    except Exception as ex:
        raise ex


async def producer(message):
    try:
        req = Request()
        req.ParseFromString(message)

        if req.type == MessageTypeRequest.Name(0):
            return await get_devices_func()

        elif req.type == MessageTypeRequest.Name(1):
            return await get_device_data_func(req.devicedata)

        elif req.type == MessageTypeRequest.Name(2):
            return await get_device_history_func(req.devicehistory)

        elif req.type == MessageTypeRequest.Name(3):
            return await get_dev_prof_id()

        elif req.type == MessageTypeRequest.Name(4):
            return await get_apps()

        elif req.type == MessageTypeRequest.Name(5):
            return await create_device_request(req.create_device)

        elif req.type == MessageTypeRequest.Name(6):
            return await get_device_type_list()

        elif req.type == MessageTypeRequest.Name(7):
            return await get_plant_list()

        else:
            return "Bad function name"
    except Exception as ex:
        logger.error(ex)
        traceback.print_exc()
        return 'For more details open error.log in working directory'


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
