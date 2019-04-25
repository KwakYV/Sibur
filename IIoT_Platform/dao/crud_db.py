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
    raise


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
        logger.info('Committed info to Data_table')
    except Exception as ex:
        logger.error(ex)
        raise


def commit_device_table(create_device_request):
    try:
        data = Device(
            deveui=bytes.fromhex(create_device_request.dev_eui),
            deveuistr=create_device_request.dev_eui,
            name=create_device_request.name,
            devicetypeid=get_device_type_id(create_device_request.type),
            factoryid=get_factory_id(create_device_request.plant),
        )
        s.add(data)
        s.commit()
    except Exception as exception:
        logger.error(exception)
        raise


def get_device_id(dev):
    logger.info('Reading Device_table')
    try:
        data_device = s.query(Device).filter(Device.deveui == bytes.fromhex(dev)).first()
        logger.info('Found the device with dev_eui - {}'.format(dev))
    except Exception as ex:
        logger.error(ex)
        raise
    return data_device.id


def get_measurement_id(measurement):
    data_m_id = s.query(Measurement).filter(Measurement.code == measurement).first()
    return data_m_id.id


def get_device_type_id(type_code):
    data_type_id = s.query(Devicetype).filter(Devicetype.code == type_code).first()
    return data_type_id.id


def get_factory_id(plant):
    data_factory_id = s.query(Factory).filter(Factory.code == plant).first()
    return data_factory_id.id


def read_gateway_table(gate_id):
    logger.info('Reading Gateway_table')
    try:
        h = bytearray.fromhex(gate_id)
        data_gateway = s.query(Gateway).filter(Gateway.fmwid == h)[0]
        logger.info('Found gateway_id')
    except Exception as ex:
        logger.error(ex)
        raise
    return data_gateway.id


def delete_device_db(dev_eui):
    try:
        s.rollback()
        data_device = s.query(Device).filter(Device.deveui == bytes.fromhex(dev_eui)).first()
        s.delete(data_device)
        s.commit();
    except Exception as exception:
        logger.error(exception)
        raise


def get_port_list(type_id):
    port_list = s.query(Port).filter(Port.devicetype_id == type_id)
    return list(port_list)


def create_sensor(create_device_request):
    try:
        device_id = get_device_id(create_device_request.dev_eui)
        port_list = get_port_list(get_device_type_id(create_device_request.type))
        for port in port_list:
            sensor = Sensor(device_id=device_id, port_id=port.id)
            s.add(sensor)
        s.commit();
    except Exception as exception:
        logger.error(exception)
        raise

