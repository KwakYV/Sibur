from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Данную часть необходимо вывести в конфигурационный файл, чтобы можно было настраивать из вне.
engine = create_engine(
    "postgres+psycopg2://postgres:digitalize1830@localhost:5432/IoT",
    isolation_level="READ UNCOMMITTED"
)

Session = sessionmaker(bind=engine)
s = Session()

from IIoT_Platform.mqtt_for_db.Entities import *

def comit_Data_Table(devid, gateid, bytedata, effdt, ppndt, fcntup, freq, rssi, sf, snr, value):
    data = Data(
        devid = devid,
        gateid = gateid,
        data = bytedata,
        effdt = effdt,
        ppndt = ppndt, #'2017-06-22 20:10:25-07',
        fcntup = fcntup,
        freq = freq,
        rssi = rssi,
        sf = sf,
        snr = snr,
        value = value,
    )
    s.add(data)
    s.commit()

def read_Device_table(dev):
    device_id = 0
    data_Device = s.query(Device).filter(Device.deveui == dev)
    for device in data_Device:
        device_id = device.id
        device_typeid = device.devicetypeid
    print('ahahha', device_id)
    return device_id

def read_Gateway_table():
    gateway_id = 0
    data_gateway = s.query(Gateway).filter(Gateway.id == 1)
    for gateway in data_gateway:
        gateway_id = gateway.fmwid
    print('gateway_id', gateway_id)
    return gateway_id

def example(deveui):
    device_type = deveui
    data_Device = s.query(Device).filter(Device.deveui == device_type)
    for device in data_Device:
        device_type = device.devicetypeid
    return device_type