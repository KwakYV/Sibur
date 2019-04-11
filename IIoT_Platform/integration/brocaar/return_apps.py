import grpc
import json

from protos.aps import application_pb2
from protos.aps import application_pb2_grpc
from protos.aps import deviceProfile_pb2
from protos.aps import deviceProfile_pb2_grpc

from google.protobuf.json_format import MessageToJson

def connection():
    with open('/Users/erguj/git_rep_2/IIoT_Platform/grpc_lora_test/http-key.pem', 'rb') as f:
        creds = grpc.ssl_channel_credentials(f.read())
        jwt = grpc.access_token_call_credentials('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJsb3JhLWFwcC1zZXJ2ZXIiLCJhdWQiOiJsb3JhLWFwcC1zZXJ2ZXIiLCJzdWIiOiJ1c2VyIiwidXNlcm5hbWUiOiJhZG1pbiJ9.sBe3chmhhgMaDBq-W-g6OicAA-aMFdW46D2udG1oVVI')
        comp = grpc.composite_channel_credentials(creds, jwt)
    return comp

def run_apps(comp):
    with grpc.secure_channel('lpwa.ru:8080', comp) as conn:
        stub = application_pb2_grpc.ApplicationServiceStub(conn)
        response = stub.List(application_pb2.ListApplicationRequest(limit=10, offset=0))
    return response

def run_device_profile(comp):
    with grpc.secure_channel('lpwa.ru:8080', comp) as conn:
        stub = deviceProfile_pb2_grpc.DeviceProfileServiceStub(conn)
        response = stub.List(deviceProfile_pb2.ListDeviceProfileRequest(limit=10, offset=0))
    return response

def apps_id(protofile):
    jsonObj = MessageToJson(protofile)
    a = json.loads(jsonObj)['result'] #['result']
    d = dict()
    count = len(a)
    for i in range(count):
        d[a[i]['name']] = a[i]['id']  #d['applicationID'] = a[i]['id']
    return d

def device_prof_id(protofile):
    jsonObj = MessageToJson(protofile)
    a = json.loads(jsonObj)['result']  # ['result']
    c = dict()
    count = len(a)
    for i in range(count):
        c[a[i]['name']] = a[i]['id']
    return c

if __name__ == '__main__':
    print(apps_id(run_apps(connection())))
    print(device_prof_id(run_device_profile(connection())))