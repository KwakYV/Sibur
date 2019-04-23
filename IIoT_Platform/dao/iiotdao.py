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
        select t.deveui, t.value
        from
        (
        select first_value(d.id) over (partition by devid order by ppndt desc) val, d.*, dev.deveuistr deveui
        from iiot.data d
        join iiot.device dev on d.devid = dev.id and dev.deveuistr in (:lst)
        ) t where  t.val = t.id
    '''
    session = Session()
    # session.execute(text(sql), params={"lst": devlist}) - данная конструкция не заработала
    #  запрос возвращает пустое множество, поэтому пошли в лоб !!!
    device_data = session.execute(text(sql.replace(':lst',devlist))).fetchall()
    return device_data


def gethistory(devlist, ts):
    sql = """
        select dev.deveuistr deveui, d.ppndt ts, COALESCE(d.value,0.0)
        from iiot.data d
        join iiot.device dev on d.devid = dev.id and dev.deveuistr in (:lst)
        where d.effdt < to_timestamp(:ts) AT TIME ZONE 'UTC'
    """
    repl = sql.replace(":lst", devlist).replace(":ts", str(ts.seconds))
    session = Session()
    history = session.execute(text(repl)).fetchall()
    return list(history)

