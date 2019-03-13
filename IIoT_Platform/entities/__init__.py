from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Данную часть необходимо вывести в конфигурационный файл, чтобы можно было настраивать из вне.
engine = create_engine(
    "postgres://iiot:iiot@192.168.10.11/iiot",
    isolation_level="READ UNCOMMITTED"
)

Session = sessionmaker(bind=engine)

from entities.Entities import *