from protos.iiot_pb2 import *
from dao.iiotdao import getdevices, getdevicedata, gethistory
from integration.brocaar.lora_app_server.apps_methods import *
from integration.brocaar.lora_app_server.connection import *
from dao.crud_db import *
import time
from protos.aps import device_pb2


def getDevices():
    devices = getdevices()
    client_response = ClientDevicesResponse()
    for device in devices:
        sensor = client_response.sensors.add()
        sensor.devEui = device[0]
        sensor.description = device[1]
    response = Response(type=MessageTypeResponse.Name(0), devicelist=client_response)
    return response.SerializeToString()


def getDeviceData(data):
    devicedata = getdevicedata(data)
    res_device_data = DeviceDataResponse()
    for devdata in devicedata:
        sensor = res_device_data.sensors.add()
        sensor.devEui = devdata[0]
        #TODO: Parse payLoad if there is no parsed data
        sensor.temperature = devdata[1]
    response = Response(type=MessageTypeResponse.Name(1), devicedata=res_device_data)
    return response.SerializeToString()


def getDeviceDataHistory(dev_lst, ts):
    history = gethistory(dev_lst, ts)
    hist_response = DeviceDataHistoryResponse()
    dict = {}
    for val in history:
        if val[0] in list(dict.keys()):
            dict[val[0]].append((val[1],val[2]))
        else:
            dict.update({val[0]: [(val[1],val[2])]})
    for devEui, values in dict.items():
        sensor = hist_response.sensors.add()
        sensor.devEui = devEui
        for val in values:
            hist = sensor.history.add()
            hist.ts.seconds = int(time.mktime(val[0].timetuple()))
            hist.value = float(val[1])
    response = Response(type=MessageTypeResponse.Name(2), devicehistory=hist_response)
    return response.SerializeToString()


def getDeviceProfileID():
    dict_device_profile = device_prof_id(connection())
    client_response = DeviceProfileResponse()
    for key, value in dict_device_profile.items():
        prof = client_response.profile.add()
        prof.name = str(key)
        prof.id = str(value)
    response = Response(type=MessageTypeResponse.Name(3), devprofid=client_response)
    return response.SerializeToString()

def getApps():
    dict_apps = apps_id(connection())
    client_response = AppsResponse()
    for key, value in dict_apps.items():
        prof = client_response.app.add()
        prof.name = str(key)
        prof.appsid = str(value)
    response = Response(type=MessageTypeResponse.Name(4), apps=client_response)
    return response.SerializeToString()
# Create device function
# create_device_request - CreateDeviceRequest message from iiot.proto
#
def create_device_func(create_device_request):
    #print('hey')
    device_request = device_pb2.CreateDeviceRequest()
    device_request.device.dev_eui = create_device_request.dev_eui
    #print(create_device_request.dev_eui)
    device_request.device.name = create_device_request.name
    device_request.device.description = create_device_request.name

    create_keys_request = device_pb2.CreateDeviceKeysRequest()
    create_keys_request.device_keys.dev_eui = create_device_request.dev_eui
    create_keys_request.device_keys.nwk_key = create_device_request.appkey

    try:
        conn = connection()
        app_id = get_application_id(conn, create_device_request.application)
        profile_id = get_profile_id(conn, create_device_request.profile)
        device_request.device.application_id = app_id
        device_request.device.device_profile_id = profile_id
        create_device(conn, device_request)
        create_keys(conn, create_keys_request)
    except Exception as ex:
        raise ex
'''
    try:
        comit_Device_Table(device_request.device.deveui, )
'''