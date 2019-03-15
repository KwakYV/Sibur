from protos.iiot_pb2 import *
from dao.iiotdao import *



def getDevices():
    devices = getdevices()
    client_response = ClientDevicesResponse()
    for device in devices:
        sensor = client_response.sensors.add()
        sensor.devEui = device[0]
        sensor.description = device[1]
    response = Response(type='get_devices', devicelist=client_response)
    return response.SerializeToString()


def getDeviceData(data):
    devicedata = getdevicedata(data)
    res_device_data = DeviceDataResponse()
    for devdata in devicedata:
        sensor = res_device_data.sensors.add()
        sensor.devEui = devdata[0]
        #TODO: Parse payLoad if there is no parsed data
        sensor.temperature = 23.4
    response = Response(type='get_device_data', devicedata=res_device_data)
    return response.SerializeToString()