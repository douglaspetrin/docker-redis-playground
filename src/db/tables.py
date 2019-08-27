from sqlalchemy import Column, Integer, String, Sequence
from src.db.setup import Base, engine


class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(20))
    fullname = Column(String(20))
    nickname = Column(String(20))


class Account(Base):

    __tablename__ = 'accounts'

    id = Column(Integer, Sequence('account_id_seq'), primary_key=True)
    type = Column(String(10))
    price = Column(String(6))


class Candle(Base):

    __tablename__ = 'candles'

    id = Column(Integer, Sequence('candle_id_seq'), primary_key=True)
    symbol = Column(String(10))
    price = Column(String(6))


class MigrateTables:

    @staticmethod
    def run():
        return Base.metadata.create_all(engine)


