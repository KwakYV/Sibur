import json
from datetime import datetime
import datetime
from dao.crud_db import *
import base64
import logging as lg
import logging.handlers as handlers

logger = lg.getLogger('parser_mqtt.py')
logger.setLevel(lg.INFO)
formatter = lg.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(funcName)s')

loghandler = handlers.RotatingFileHandler('../server/info_launcher.log', maxBytes=20000000, backupCount=10)
loghandler.setFormatter(formatter)

errorhandler = handlers.RotatingFileHandler('../server/error_launcher.log', maxBytes=20000000, backupCount=10)
errorhandler.setLevel(lg.ERROR)
errorhandler.setFormatter(formatter)

logger.addHandler(loghandler)
logger.addHandler(errorhandler)


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


def gateway_id_innolabs(js):
    h = js['gatewayID']
    gate_id = bytearray.fromhex(h)
    return gate_id


def timestamp():
    t = datetime.now()
    return t


def data_hex_innolabs(js):
    if js['sensorTypeName'] == 'ThingenixSensorHub':
        hex = js['SensorDataHex'][0]['ValueHex']
    else:
        hex = js['dataHex']
    ba = bytearray.fromhex(hex)
    return ba


def data_bytes(json):
    try:
        data = base64.b64decode(json['data'])
        data = data.hex()
        data = bytes.fromhex(data)
        return data
    except Exception as ex:
        logger.error(ex)
        raise


def gateway_id(json):
    try:
        gate_id = json['rxInfo'][0]['gatewayID']
        return gate_id
    except Exception as ex:
        logger.error(ex)
        raise


def timest(json):
    try:
        time = json['rxInfo'][0]['time']
        return time
    except Exception as ex:
        logger.error(ex)
        raise


def fcnt(json):
    try:
        fcnt = int(json['fCnt'])
        return fcnt
    except Exception as ex:
        logger.error(ex)
        raise


def freq(json):
    try:
        freq = int(json['txInfo']['frequency'])
        return freq
    except Exception as ex:
        logger.error(ex)
        raise


def rssi(json):
    try:
        rssi = int(json['rxInfo'][0]['rssi'])
        return rssi
    except Exception as ex:
        logger.error(ex)
        raise


def snr(json):
    try:
        snr = float(json['rxInfo'][0]['loRaSNR'])
        return snr
    except Exception as ex:
        logger.error(ex)
        raise


def values(json):
    try:
        return_val = {
            "1": value_td_11(json),
            "2": value_si_22(json),
            "3": value_rising_hf(json),
        }
        return return_val[str(find_device_type_id(deveui(json)))]
    except Exception as ex:
        logger.error(ex)
        raise


def value_si_22(json):
    try:
        val = json['data']
        value = base64.b64decode(val)
        value = value.hex()
        value = bytes.fromhex(value[14:16])
        value = int.from_bytes(value, byteorder='little', signed=True)
        return float(value)
    except Exception as ex:
        logger.error(ex)
        raise


def value_rising_hf(json):
    try:
        val = json['data']
        value = base64.b64decode(val)
        value = value.hex()
        humidity = bytes.fromhex(value[6:8])
        humidity = int.from_bytes(humidity, byteorder='big', signed=False)
        humidity = float(((125 * humidity) / (2 ** 8)) - 6)
        return humidity
    except Exception as ex:
        logger.error(ex)
        raise


def value_td_11(json):
    try:
        val = json['data']
        value = base64.b64decode(val)
        value = value.hex()
        value_td = bytes.fromhex(value[14:18])
        value_td = int.from_bytes(value_td, byteorder='little', signed=True)
        t_td = float(value_td / 10)
        return t_td
    except Exception as ex:
        logger.error(ex)
        raise


def data_val(js):
    if js['sensorTypeName'] == 'ThingenixSensorHub':
        t = js['InternalSensors'][3]['Value']
    else:
        t = js['InternalSensors'][1]['Value']
    val = float(t)  # type(t) is string
    return val  # изменение типа по str to int


def parse_payload_data(data):
    try:
        dev_eui = data['devEUI'] # json['devEUI']
        sensors = get_sensor_list(dev_eui)
        data_object_list = []
        logger.info('Forming data_object_list')
        for sensor in sensors:
            data = Data(
                sensor_id=sensor.id,
                gateid=read_gateway_table(gateway_id(data)),
                data=data_bytes(data),
                effdt=timest(data),
                ppndt=timest(data),
                fcntup=fcnt(data),
                freq=freq(data),
                rssi=rssi(data),
                sf=7,
                snr=snr(data),
                value=values(data),
            )
            data_object_list.append(data)
            logger.info('Formed data_object_list')
        return data_object_list
    except Exception as ex:
        logger.error(ex)
        raise