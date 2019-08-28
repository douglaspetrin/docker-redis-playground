import sqlalchemy
from sqlalchemy.orm import sessionmaker
from src.db.tables import Base
from src.db.tables import User, Candle


class Start(object):
    def __init__(self, localhost=None, database='doug_db', user='root', password='root'):
        """ Starts with MySQL address"""
        self.localhost = localhost
        self.database = database
        self.user = user
        self.password = password
        self.engine = self._create_engine()
        self.session_maker = sessionmaker(bind=self.engine)
        self.session = self.session_maker()
        self.conn = self.engine.connect()

    def _create_engine(self):
        """ Creates an engine"""
        return sqlalchemy.create_engine('mysql+mysqlconnector://{}:{}@{}/{}'.format(
            self.user, self.password, self.localhost, self.database), echo=True)

    def create_all_tables(self):
        """ Creates all tables in the engine """
        return Base.metadata.create_all(self.engine)

    def _add_to_table(self, table=None, arg1=None, arg2=None):
        """ Adds data to table"""

        if table == "User":
            d = User(name=arg1, fullname=arg2, nickname=arg2)

        if table == "Candle":
            d = Candle(symbol=arg1, price=arg2)

        if table is None:
            d = None

        return d

    def add(self, table=None, arg1=None, arg2=None):
        """ Adds data to the tables"""
        data = self._add_to_table(table, arg1, arg2)
        return self.session.add(data)

    def commit_session(self):
        """ Commits the open session"""
        return self.session.commit()
