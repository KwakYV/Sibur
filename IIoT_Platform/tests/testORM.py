'''
from __future__ import print_function

from entities import *
from sqlalchemy import text
from controller.protocontroller import *

from protos.iiot_pb2 import *
from protos.iiot_pb2_grpc import *

import grpc
session = Session()




#gateway = en.Gateway(code='B031821', name='Office Kerlink', desc='Kerlink Wirenet station', fmwid=b'B031821', factoryid=1)

#session.add(gateway)
#session.commit()

#factory = session.query(Factory).all()
#print(factory[0].gateways[1].fmwid)

result = getDevices()
print(result)





#from examples.python.helloworld import helloworld_pb2
#from examples.python.helloworld import helloworld_pb2_grpc



def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') aps channel:
        stub = IotStub(channel)
        response = stub.GetDevices(DeviceDataRequest(cmd='get_devices'))
    print(response.sensors[0].devEui)
    print(response.sensors[0].description)


if __name__ == '__main__':
    run()

'''



import asyncio
import websockets
from protos.iiot_pb2 import *
import json
import time as tm
from google.protobuf.timestamp_pb2 import *
from google.protobuf.json_format import MessageToJson


async def main():
    async with websockets.connect('ws://127.0.0.1:8766/') as ws: #ws://192.168.10.11:8761/
        list = ['343438356F37750C', '343438356B37620E', '001bc5035000043a']
        tms = Timestamp()
        tms.seconds = 1542716804000
        devDataReq = DeviceDataHistoryRequest(devEuiList=list, ts=tms)

        req = Request(type=MessageTypeRequest.Name(2), devicehistory=devDataReq )
        await ws.send(req.SerializeToString())
        response = await ws.recv()
        #print(response)
        res = Response()
        res.ParseFromString(response)
        print(res.type)
        devices = res.devicehistory
        print(devices.sensors)

async def notmain():
    async with websockets.connect('ws://127.0.0.1:8766/') as ws: #ws://192.168.10.11:8761/
        req = Request(type=MessageTypeRequest.Name(3))
        await ws.send(req.SerializeToString())
        response = await ws.recv()
        #print(response)
        res = Response()
        print(res)
        res.ParseFromString(response)
        print(res.type)
        devices = res.devprofid
        print(devices.profile)

async def notmain_2():
    async with websockets.connect('ws://127.0.0.1:8766/') as ws: #ws://192.168.10.11:8761/
        req = Request(type=MessageTypeRequest.Name(5))
        await ws.send(req.SerializeToString())
        response = await ws.recv()
        #print(response)
        res = Response()
        print(res)
        res.ParseFromString(response)
        print(res.type)
        devices = res.devprofid
        print(devices.profile)

async def notmain_1():
    async with websockets.connect('ws://127.0.0.1:8766/') as ws: #ws://192.168.10.11:8761/
        req = Request(type=MessageTypeRequest.Name(4))
        await ws.send(req.SerializeToString())
        response = await ws.recv()
        #print(response)
        res = Response()
        #print(res)
        res.ParseFromString(response)
        print(res.type)
        devices = res.apps
        dapp = MessageToJson(devices)
        print(type(dapp))
        js = json.loads(dapp)
        print(js['app'])

asyncio.get_event_loop().run_until_complete(notmain_1())
"""

from protos.iiot_pb2 import *

print()

"""