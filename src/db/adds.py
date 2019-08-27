from sqlalchemy.orm import sessionmaker
from src.db.setup import engine
from src.db.tables import User, Candle

Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()

ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
jj_user = User(name='jhon', fullname='Jhon Jones', nickname='jhony')

symbol1 = Candle(symbol='PETR4', price='30.1')
symbol2 = Candle(symbol='PETR5', price='32.1')

session.add(ed_user)
session.add(jj_user)

session.add(symbol1)
session.add(symbol2)

# session.add_all(
#                   User(name='jhon', fullname='Jhon Jones', nickname='jhony'),
#                   User(name='jhon', fullname='Jhon Jones', nickname='jhony'),
#                   User(name='jhon', fullname='Jhon Jones', nickname='jhony'))

# our_user = session.query(User).filter_by(name='jhon').first()

# dirty = session.dirty
# new = session.new
session.commit()