from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(20))
    fullname = Column(String(20))
    nickname = Column(String(20))


class Candle(Base):

    __tablename__ = 'candles'

    id = Column(Integer, Sequence('candle_id_seq'), primary_key=True)
    symbol = Column(String(10))
    price = Column(String(6))


class Opaa(Base):

    __tablename__ = 'opaa'

    id = Column(Integer, Sequence('opaa_id_seq'), primary_key=True)
    symbol = Column(String(20))
    price = Column(String(20))



