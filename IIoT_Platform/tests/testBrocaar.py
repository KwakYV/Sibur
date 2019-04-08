
import grpc
from protos.aps import user_pb2
from protos.aps import user_pb2_grpc


def run():
    gateway_request = ns_pb2.Gateway()
    gateway_request.id = bytes(bytearray.fromhex('7276ff000b031819'))
    with grpc.insecure_channel('192.168.10.28:8080') as channel:
        res = ns_pb2_grpc.NetworkServerServiceStub(channel).GetVersion(gateway_request)
        print(res)

if __name__ == '__main__':
    run()
