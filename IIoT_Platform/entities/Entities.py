from sqlalchemy import Column, String, Integer, ForeignKey, Sequence, create_engine, inspect
from sqlalchemy.dialects.postgresql import *
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Data(Base):
    __tablename__='DATA'
    __table_args__ = {'extend_existing': True}
    id = Column('ID', Integer, Sequence('iiotSeq'), primary_key=True)
    devid = Column('DEV_ID', Integer, nullable=False)
    gateid = Column('GATE_ID', Integer, nullable=False)
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
    id = Column('ID', Integer, Sequence('iiotSeq'), primary_key=True)
    code = Column('CODE', String(50), nullable=False)
    name = Column('NAME', String(150))
    desc = Column('DESC', String(300))
    gateways = relationship("Gateway", backref('FACTORY'))

class Gateway(Base):
    __tablename__='GATEWAY'
    id = Column('ID', Integer, Sequence('iiotSeq'), primary_key=True)
    code = Column('CODE', String(50), nullable=False)
    name = Column('NAME', String(100))
    desc = Column('DESC', String(150))
    fmwid = Column('FMW_ID', BYTEA, nullable=False)
    factoryid = Column('FACTORY_ID', Integer, ForeignKey('FACTORY.ID'), nullable=False)



factory = Factory(code='ZapSib', name='ZapSibNefteHim', desc='Завод ЗапСибНефтеХим')