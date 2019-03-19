from protos.iiot_pb2 import *
from dao.iiotdao import getdevices, getdevicedata, gethistory
from google.protobuf.timestamp_pb2 import *
import time



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
    response = Response(type='get_device_history', devicehistory=hist_response)
    return response.SerializeToString()