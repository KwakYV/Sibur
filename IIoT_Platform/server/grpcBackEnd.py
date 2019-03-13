from concurrent import futures
import time
import grpc

from protos.iiot_pb2 import *
from protos.iiot_pb2_grpc import *


_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Iot(IotServicer):
    def GetDevices(self, request, context):
        response = DeviceDataResponse()
        response.cmd = request.cmd
        sensor = response.sensors.add()
        sensor.devEui = 'asdf;lkje757993'
        sensor.description = 'Test protobuf'
        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_IotServicer_to_server(Iot(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()