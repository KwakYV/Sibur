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
    with grpc.insecure_channel('localhost:50051') as channel:
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
import json as jsn
import time as tm
from google.protobuf.timestamp_pb2 import *


async def main():
    async with websockets.connect('ws://192.168.10.15:8761/') as ws:
        list = ['343438356F37750C', '343438356B37620E']
        tms = Timestamp()
        tms.seconds = 1542716804000
        devDataReq = DeviceDataHistoryRequest(devEuiList=list, ts=tms)

        req = Request(type='get_device_history', devicehistory=devDataReq )
        await ws.send(req.SerializeToString())
        response = await ws.recv()
        #print(response)
        res = Response()
        res.ParseFromString(response)
        print(res.type)
        devices = res.devicehistory
        print(devices.sensors)



asyncio.get_event_loop().run_until_complete(main())