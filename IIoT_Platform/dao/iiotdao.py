from entities import *
from sqlalchemy import text


def getdevices():
    sql = '''
        select deveuistr, name 
        from iiot.device
    '''
    session = Session()
    devices = session.execute(text(sql)).fetchall()
    return devices


def getdevicedata(devlist):
    sql='''
        select t.deveui, t.data
        from
        (
        select first_value(d.id) over (partition by devid order by ppndt desc) val, d.*, dev.deveuistr deveui
        from iiot.data d
        join iiot.device dev on d.devid = dev.id and dev.deveuistr in (:lst)
        ) t where  t.val = t.id
    '''
    session = Session()
    devicedata = session.execute(text(sql), {"lst":devlist}).fetchall()
    return devicedata
