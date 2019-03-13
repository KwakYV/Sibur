from sqlalchemy import Column, String, Integer, ForeignKey, Sequence
from sqlalchemy.dialects.postgresql import *
from sqlalchemy.orm import relationship, backref
from entities import Base

__all__=['Data', 'Factory', 'Gateway', 'Deviceparams', 'Devicetype', 'Device', 'Lndevparam', 'Measurement']

class Data(Base):
    __tablename__='DATA'
    __table_args__ = {'extend_existing': True}
    id = Column('ID', Integer, Sequence('iiotSeq'), primary_key=True, nullable=False)
    devid = Column('DEV_ID', Integer, ForeignKey('Device.ID'), nullable=False)
    gateid = Column('GATE_ID', Integer, ForeignKey('GATEWAY.ID'), nullable=False)
    data = Column('DATA', BYTEA)
    effdt = Column('EFF_DT', DATE)
    ppndt = Column('PPN_DT', TIMESTAMP)
    fcntup = Column('FCNTUP', Integer)
    freq = Column('FREQ', Integer)
    rssi = Column('RSSI', Integer)
    sf = Column('SF', Integer)
    snr = Column('SNR', NUMERIC(precision=10,scale=4))

class Factory(Base):
    __tablename__='FACTORY'
    id = Column('ID', Integer, Sequence('iiotSeq'), primary_key=True, nullable=False)
    code = Column('CODE', String(50), nullable=False)
    name = Column('NAME', String(150))
    desc = Column('DESC', String(300))
    gateways = relationship('Gateway', backref='FACTORY')
    devices = relationship('Device', backref='FACTORY')


class Gateway(Base):
    __tablename__='GATEWAY'
    id = Column('ID', Integer, Sequence('iiotSeq'), primary_key=True, nullable=False)
    code = Column('CODE', String(50), nullable=False)
    name = Column('NAME', String(100))
    desc = Column('DESC', String(150))
    fmwid = Column('FMW_ID', BYTEA, nullable=False)
    factoryid = Column('FACTORY_ID', Integer, ForeignKey('FACTORY.ID'), nullable=False)


class Deviceparams(Base):
    __tablename__='DEVICEPARAMS'
    id = Column('ID', Integer, Sequence('iiotSeq'), primary_key=True, nullable=False)
    code = Column('CODE', String(50), nullable=False)
    name = Column('NAME', String(50))
    desc = Column('DESC', String(100))

class Devicetype(Base):
    __tablename__='DEVICETYPE'
    id = Column('ID', Integer, Sequence('iiotSeq'), primary_key=True, nullable=False)
    code = Column('CODE', String(50), nullable=False)
    name = Column('NAME', String(100))
    desc = Column('DESC', String(150))
    vendor = Column('VENDOR', String(100))
    payloadlen = Column('PAYLOADLEN', Integer)

class Device(Base):
    __tablename__ = 'Device'
    id = Column('ID', Integer, Sequence('iiotSeq'), primary_key=True, nullable=False)
    deveui = Column('DEVEUI', BYTEA, nullable=False)
    deveuistr = Column('DEVEUI_STR', String(50), nullable=False)
    name = Column('NAME', String(250))
    devicetypeid = Column('DEVICE_TYPE_ID', Integer, ForeignKey('DEVICETYPE.ID'))
    measurementid = Column('MEASUREMENT_ID', Integer, ForeignKey('MEASUREMENT.ID'), nullable=False)
    factoryid = Column('FACTORY_ID', Integer, ForeignKey('FACTORY.ID'), nullable=False)

class Lndevparam(Base):
    __tablename__='LN_DEVPARAM_DEV'
    paramid = Column('DEVPARAM_ID', Integer, ForeignKey('DEVICEPARAMS.ID'), primary_key=True, nullable=False)
    devid = Column('DEV_ID', Integer, ForeignKey('Device.ID'), primary_key=True, nullable=False)
    value = Column('PARAM_VAL', NUMERIC)
    effdt = Column('EFF_DT', DATE)

class Measurement(Base):
    __tablename__='MEASUREMENT'
    id = Column('ID', Integer, Sequence('iiotSeq'), primary_key=True, nullable=False)
    code = Column('CODE', String(50), nullable=False)
    desc = Column('DESC', String(100))


#factory = Factory(code='ZapSib', name='ZapSibNefteHim', desc='Завод ЗапСибНефтеХим')