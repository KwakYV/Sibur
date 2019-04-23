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


def commit_data_table(devid, gateid, bytedata, effdt, ppndt, fcntup, freq, rssi, sf, snr, value):
    logger.info('Committing info to Data_table')
    data = Data(
        devid=devid,
        gateid=gateid,
        data=bytedata,
        effdt=effdt,
        ppndt=ppndt,
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


def commit_device_table(create_device_request):
    data = Device(
        deveui=bytes.fromhex(create_device_request.dev_eui),
        deveuistr=create_device_request.dev_eui,
        name=create_device_request.name,
        devicetypeid=get_device_type(create_device_request.type),
        measurementid=get_measurement_id(create_device_request.measurement),
        factoryid=get_factory_id(create_device_request.plant),
        portnumber=0 #TODO: Prepare algorithm for getting device's port number
    )
    s.add(data)
    s.commit()


def get_device_id(dev):
    logger.info('Reading Device_table')
    try:
        data_device = s.query(Device).filter(Device.deveui == dev)[0]
        logger.info('Found the device with dev_eui - {}'.format(dev))
        return data_device.id
    except Exception as ex:
        logger.error(ex)


def get_measurement_id(measurement):
    data_m_id = s.query(Measurement).filter(Measurement.code == measurement)[0]
    return data_m_id.id


def get_device_type(type_code):
    data_type_id = s.query(Devicetype).filter(Devicetype.code == type_code)[0]
    return data_type_id.id


def get_factory_id(plant):
    data_factory_id = s.query(Factory).filter(Factory.code == plant)[0]
    return data_factory_id.id


def read_gateway_table(gateid):
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


def delete_device_db(dev_eui):
    try:
        data_device = s.query(Device).filter(Device.deveui == dev_eui)[0]
        data_device.delete(synchronize_session=False)
    except Exception as exception:
        raise exception
