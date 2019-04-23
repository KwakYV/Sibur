from sqlalchemy.orm import sessionmaker
from entities import *
import logging as lg
import logging.handlers as handlers
#from entities.Entities import *

logger = lg.getLogger('crud_db.py')
logger.setLevel(lg.INFO)
formatter = lg.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(funcName)s')

loghandler = handlers.RotatingFileHandler('../server/info_launcher.log', maxBytes=20000000, backupCount=10)
loghandler.setFormatter(formatter)

errorhandler = handlers.RotatingFileHandler('../server/error_launcher.log', maxBytes=20000000, backupCount=10)
errorhandler.setLevel(lg.ERROR)
errorhandler.setFormatter(formatter)

logger.addHandler(loghandler)
logger.addHandler(errorhandler)


try:
    logger.info('Starting session ... ')
    s = Session()
    logger.info('Started session ... ')
except Exception as ex:
    logger.error(ex)


def comit_Data_Table(devid, gateid, bytedata, effdt, ppndt, fcntup, freq, rssi, sf, snr, value):
    logger.info('Commiting info to Data_table')
    data = Data(
        devid=devid,
        gateid=gateid,
        data=bytedata,
        effdt=effdt,
        ppndt=ppndt, #'2017-06-22 20:10:25-07',
        fcntup=fcntup,
        freq=freq,
        rssi=rssi,
        sf=sf,
        snr=snr,
        value=value,
    )
    try:
        s.add(data)
        s.commit()
        logger.info('Commited info to Data_table')
    except Exception as ex:
        logger.error(ex)

def comit_Device_Table(deveui, deveuistr, name, devicetypeid, measurementid, factoryid):
    data = Device(
        deveui=deveui,
        deveuistr=deveuistr,
        name=name,
        devicetypeid=devicetypeid,
        measurementid=measurementid,  # '2017-06-22 20:10:25-07',
        factoryid=factoryid,
    )
    s.add(data)
    s.commit()

def read_Device_table(dev):
    logger.info('Reading Device_table')
    try:
        data_Device = s.query(Device).filter(Device.deveui == dev)[0]
        logger.info('Found the Device_deveui')
        return data_Device.id
    except Exception as ex:
        logger.error(ex)

def read_Measures():
    data_m_id = s.query(Measurement).filter(Measurement.description == 'Temperature')[0]
    return data_m_id.id

def read_DeviceType():
    data_type_id = s.query(Devicetype).filter(Devicetype.vendor == 'Vega')[0]
    return data_type_id.id

def read_Factoryid():
    data_factoryid = s.query(Factory).filter(Factory.name == 'ZapSib')[0]
    return data_factoryid.id

def read_Gateway_table(gateid):
    logger.info('Reading Gateway_table')
    try:
        h = bytearray.fromhex(gateid)
        data_gateway = s.query(Gateway).filter(Gateway.fmwid == h)[0]
        logger.info('Found gateway_id')
        return data_gateway.id
    except Exception as ex:
        logger.error(ex)

def example(deveui):
    device_type = deveui
    data_Device = s.query(Device).filter(Device.deveui == device_type)
    for device in data_Device:
        device_type = device.devicetypeid
    return device_type

