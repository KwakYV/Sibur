from sqlalchemy.orm import sessionmaker
from entities import *

#Session = sessionmaker(bind=engine)
s = Session()

from entities.Entities import *

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
    data_Device = s.query(Device).filter(Device.deveui == dev)[0]
    return data_Device.id

def read_Gateway_table(gateid):
    h = bytearray.fromhex(gateid)
    data_gateway = s.query(Gateway).filter(Gateway.fmwid == h)[0]
    return data_gateway.id

def example(deveui):
    device_type = deveui
    data_Device = s.query(Device).filter(Device.deveui == device_type)
    for device in data_Device:
        device_type = device.devicetypeid
    return device_type