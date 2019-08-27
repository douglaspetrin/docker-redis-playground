from sqlalchemy.orm import sessionmaker
from src.db.setup import engine
from src.db.tables import User, Candle, Account

Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()

ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
jj_user = User(name='jhon', fullname='Jhon Jones', nickname='jhony')

symbol1 = Candle(symbol='PETR4', price='30.1')
symbol2 = Candle(symbol='PETR5', price='32.1')

account1 = Account(type='Paid', price='100')
account2 = Account(type='Paid', price='200')

session.add(ed_user)
session.add(jj_user)

session.add(symbol1)
session.add(symbol2)

session.add(account1)
session.add(account2)

session.commit()