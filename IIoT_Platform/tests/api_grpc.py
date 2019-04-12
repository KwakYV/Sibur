import grpc

from protos.aps import application_pb2
from protos.aps import application_pb2_grpc
from protos.aps import deviceProfile_pb2
from protos.aps import deviceProfile_pb2_grpc

from google.protobuf.json_format import MessageToJson
import json


'''
def run_apps(a):
    with grpc.secure_channel('lpwa.ru:8080', a) as conn:
        stub = application_pb2_grpc.ApplicationServiceStub(conn)
        response = stub.List(application_pb2.ListApplicationRequest(limit=10, offset=0))
    return response

def run_device_profile(a):
    with grpc.secure_channel('lpwa.ru:8080', a) as conn:
        stub = deviceProfile_pb2_grpc.DeviceProfileServiceStub(conn)
        response = stub.List(deviceProfile_pb2.ListDeviceProfileRequest(limit=10, offset=0))
    return response
'''