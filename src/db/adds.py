from sqlalchemy.orm import sessionmaker
from .setup import engine
from .tables import User

Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()

ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
jj_user = User(name='jhon', fullname='Jhon Jones', nickname='jhony')

session.add(ed_user)
session.add(jj_user)
# session.add_all(
#                   User(name='jhon', fullname='Jhon Jones', nickname='jhony'),
#                   User(name='jhon', fullname='Jhon Jones', nickname='jhony'),
#                   User(name='jhon', fullname='Jhon Jones', nickname='jhony'))

our_user = session.query(User).filter_by(name='jhon').first()

dirty = session.dirty
new = session.new
# session.commit()