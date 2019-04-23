from sqlalchemy import Column, String, Integer, ForeignKey, Sequence
from sqlalchemy.dialects.postgresql import *
from sqlalchemy.orm import relationship, backref
from entities import Base

__all__=['Data', 'Factory', 'Gateway', 'Deviceparams', 'Devicetype', 'Device', 'Lndevparam', 'Measurement']

class Data(Base):
    __tablename__='data'
    id = Column('id', Integer, Sequence('iiotseq'), primary_key=True, nullable=False)
    devid = Column('devid', Integer, ForeignKey('device.id'), nullable=False)
    gateid = Column('gateid', Integer, ForeignKey('gateway.id'), nullable=False)
    data = Column('data', BYTEA)
    effdt = Column('effdt', DATE)
    ppndt = Column('ppndt', TIMESTAMP)
    fcntup = Column('fcntup', Integer)
    freq = Column('freq', Integer)
    rssi = Column('rssi', Integer)
    sf = Column('sf', Integer)
    snr = Column('snr', NUMERIC(precision=10,scale=4))
    value = Column('value', NUMERIC(precision=10,scale=4)) #изменение с str to numeric

class Factory(Base):
    __tablename__='factory'
    id = Column('id', Integer, Sequence('iiotseq'), primary_key=True, nullable=False)
    code = Column('code', String(50), nullable=False)
    name = Column('name', String(150))
    description = Column('description', String(300))
    gateways = relationship('Gateway', backref='factory')
    devices = relationship('Device', backref='factory')

class Gateway(Base):
    __tablename__='gateway'
    id = Column('id', Integer, Sequence('iiotseq'), primary_key=True, nullable=False)
    code = Column('code', String(50), nullable=False)
    name = Column('name', String(100))
    description = Column('description', String(150))
    fmwid = Column('fmwid', BYTEA, nullable=False)
    factoryid = Column('factoryid', Integer, ForeignKey('factory.id'), nullable=False)

class Deviceparams(Base):
    __tablename__='deviceparams'
    id = Column('id', Integer, Sequence('iiotseq'), primary_key=True, nullable=False)
    code = Column('code', String(50), nullable=False)
    name = Column('name', String(50))
    description = Column('description', String(100))

class Devicetype(Base):
    __tablename__='devicetype'
    id = Column('id', Integer, Sequence('iiotseq'), primary_key=True, nullable=False)
    code = Column('code', String(50), nullable=False)
    name = Column('name', String(100))
    desc = Column('description', String(150))
    vendor = Column('vendor', String(100))
    payloadlen = Column('payloadlen', Integer)

class Device(Base):
    __tablename__ = 'device'
    id = Column('id', Integer, Sequence('iiotseq'), primary_key=True, nullable=False)
    deveui = Column('deveui', BYTEA, nullable=False)
    deveuistr = Column('deveuistr', String(50), nullable=False)
    name = Column('name', String(250))
    devicetypeid = Column('devicetypeid', Integer, ForeignKey('devicetype.id'))
    measurementid = Column('measurementid', Integer, ForeignKey('measurement.id'), nullable=False)
    factoryid = Column('factoryid', Integer, ForeignKey('factory.id'), nullable=False)
    portnumber = Column('portnumber', Integer, nullable=False)

class Lndevparam(Base):
    __tablename__='ln_devparam_dev'
    paramid = Column('devparamid', Integer, ForeignKey('deviceparams.id'), primary_key=True, nullable=False)
    devid = Column('devid', Integer, ForeignKey('device.id'), primary_key=True, nullable=False)
    value = Column('paramval', NUMERIC)
    effdt = Column('effdt', DATE)

class Measurement(Base):
    __tablename__='measurement'
    id = Column('id', Integer, Sequence('iiotseq'), primary_key=True, nullable=False)
    code = Column('code', String(50), nullable=False)
    description = Column('description', String(100))


#factory = Factory(code='ZapSib', name='ZapSibNefteHim', desc='Завод ЗапСибНефтеХим')