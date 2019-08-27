import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = db.create_engine('mysql+mysqlconnector://root:root@172.17.0.1/doug_db', echo=True)
conn = engine.connect()
metadata = db.MetaData()

