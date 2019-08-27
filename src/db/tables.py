from sqlalchemy import Column, Integer, String, Sequence, Numeric
from src.db.setup import Base, engine


class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(20))
    fullname = Column(String(20))
    nickname = Column(String(20))


class Candle(Base):

    __tablename__ = 'candle'

    id = Column(Integer, Sequence('candle_id_seq'), primary_key=True)
    symbol = Column(String(10))
    price = Column(String(6))


Base.metadata.create_all(engine)


