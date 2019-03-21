from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Данную часть необходимо вывести в конфигурационный файл, чтобы можно было настраивать из вне.
engine = create_engine(
    "postgres+psycopg2://postgres:digitalize1830@localhost:5432/IoT",
    isolation_level="READ UNCOMMITTED")

Session = sessionmaker(bind=engine)
s = Session()
#s.close()

from IIoT_Platform.entities.Entities import *

#Base.metadata.create_all(engine)
