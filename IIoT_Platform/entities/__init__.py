from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import configparser
#from server.launcher import logger,formatter, lg, loghandler, errorhandler
Base = declarative_base()

#postgres+psycopg2://postgres:digitalize1830@localhost:5432/IoT
#postgres://iiot:iiot@192.168.10.11/iiot

__config = configparser.ConfigParser()
__config.read('../configs/engine.properties')
__eparams=__config['engine.settings']

# Данную часть необходимо вывести в конфигурационный файл, чтобы можно было настраивать из вне.
engine = create_engine(
    __eparams['conn_string'],
    isolation_level=__eparams['isolation_level']
)

Session = sessionmaker(bind=engine)

from entities.Entities import *

