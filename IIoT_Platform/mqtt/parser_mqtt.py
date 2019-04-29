import json
from datetime import datetime
import datetime


def get_message(msg):
    spisok = []
    if 'innolabs' in msg:
        spisok.append(msg.split('\''))
    return spisok


def parser_message(spisok):
    s = spisok[0][1]
    js = json.loads(s)
    return js


def deveui(js):
    h = js['devEUI'] #001bc5035000043a 363833357b386b10
    dev_eui = bytearray.fromhex(h)
    return dev_eui


def gateway_id(js):
    h = js['gatewayID']
    gate_id = bytearray.fromhex(h)
    return gate_id


def timestamp():
    t = datetime.now()
    return t


def data_hex(js):
    if js['sensorTypeName'] == 'ThingenixSensorHub':
        hex = js['SensorDataHex'][0]['ValueHex']
    else:
        hex = js['dataHex']
    ba = bytearray.fromhex(hex)
    return ba


def data_val(js):
    if js['sensorTypeName'] == 'ThingenixSensorHub':
        t = js['InternalSensors'][3]['Value']
    else:
        t = js['InternalSensors'][1]['Value']
    val = float(t)  # type(t) is string
    return val  # изменение типа по str to int