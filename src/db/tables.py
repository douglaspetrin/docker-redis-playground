from sqlalchemy import Column, Integer, String, Sequence


class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(20))
    fullname = Column(String(20))
    nickname = Column(String(20))


