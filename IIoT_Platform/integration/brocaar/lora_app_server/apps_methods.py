from protos.aps import application_pb2
from protos.aps import application_pb2_grpc
from protos.aps import deviceProfile_pb2
from protos.aps import deviceProfile_pb2_grpc
from protos.aps import device_pb2_grpc
from google.protobuf.json_format import MessageToJson
from integration.brocaar.lora_app_server.connection import *
import json

def apps_id(conn):
    stub = application_pb2_grpc.ApplicationServiceStub(conn)
    response = stub.List(application_pb2.ListApplicationRequest(limit=10, offset=0))
    jsonObj = MessageToJson(response)
    a = json.loads(jsonObj)['result'] #['result']
    d = dict()
    count = len(a)
    for i in range(count):
        d[a[i]['name']] = a[i]['id']  #d['applicationID'] = a[i]['id']
    return d

def device_prof_id(conn):
    stub = deviceProfile_pb2_grpc.DeviceProfileServiceStub(conn)
    response = stub.List(deviceProfile_pb2.ListDeviceProfileRequest(limit=10, offset=0))
    jsonObj = MessageToJson(response)
    a = json.loads(jsonObj)['result']  # ['result']
    c = dict()
    count = len(a)
    for i in range(count):
        c[a[i]['name']] = a[i]['id']
    return c

def create_device(conn, request):
    try:
        device_pb2_grpc.DeviceServiceStub(conn).Create(request)
    except Exception as ex:
        raise ex


def create_keys(conn, request):
    try:
        device_pb2_grpc.DeviceServiceStub(conn).CreateKeys(request)
    except Exception as ex:
        raise ex

#print(apps_id(connection()))