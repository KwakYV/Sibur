from __future__ import print_function

from entities import *
from sqlalchemy import text


from protos.iiot_pb2 import *
from protos.iiot_pb2_grpc import *


session = Session()


sql = '''select f."NAME", g."CODE"
from iiot."FACTORY" f
join  iiot."GATEWAY" g on g."FACTORY_ID" = f."ID" '''

#gateway = en.Gateway(code='B031821', name='Office Kerlink', desc='Kerlink Wirenet station', fmwid=b'B031821', factoryid=1)

#session.add(gateway)
#session.commit()

#factory = session.query(Factory).all()
#print(factory[0].gateways[1].fmwid)

result = session.execute(text(sql))
print(result.fetchall())



import grpc

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