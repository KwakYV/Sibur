from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import random
Base = declarative_base()

# Данную часть необходимо вывести в конфигурационный файл, чтобы можно было настраивать из вне.
engine = create_engine(
    "postgres+psycopg2://postgres:digitalize1830@localhost:5432/IoT",
    isolation_level="READ UNCOMMITTED"
)

Session = sessionmaker(bind=engine)
s = Session()

from IIoT_Platform.entities.Entities import *

def comit_Data_Table(devid, gateid, bytedata, effdt,ppndt, fcntup, freq, rssi, sf, snr, value):
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
    spis = []
    device_id = 0
    data_Device = s.query(Device).filter(Device.deveui == dev)
    for device in data_Device:
        device_id = device.id
        device_typeid = device.devicetypeid
    print('ahahha', device_id)
    return device_id

def read_Gateway_table():
    data_Gateway = s.query(Gateway).order_by(Gateway.id.desc()).first()
    gateway_id = data_Gateway.id
    return gateway_id

def example(deveui):
    device_type = deveui
    data_Device = s.query(Device).filter(Device.deveui == device_type)
    for device in data_Device:
        device_type = device.devicetypeid
    return device_type

def read_bytes():
    id = random.randint(75, 80)
    spisok = []
    data_Device = s.query(Data).filter(Data.id == id)
    for device in data_Device:
        spisok.append(id)
        spisok.append(device.id)
        spisok.append(device.data)
    return spisok
