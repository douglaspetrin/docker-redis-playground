import random
import time
from src.redisdb.app import StartRedis
from src.db.start import StartMySQL
import json

sr = StartRedis('172.24.0.5')
sm = StartMySQL('172.24.0.4')
# class InputData(object):
#
#     """ Generates data """
#
#     def __init__(self, name, fullname, nickname):
#         self.name = name
#         self.fullname = fullname
#         self.nickname = nickname

name = [
    'Douglas',
    'Petrin',
    'Bertini'
]

fullname = [
    'Douglas P B',
    'P B Doug',
    'P B'
]

nickname = [
    'douglao',
    'doug',
    'dogras'
]

# while True:
data = '[{}, {}, {}]'.format(random.choice(name), random.choice(fullname), random.choice(nickname))
id = time.time()
sr.set_name_value(id, data)
sr_ob = sr.read_set(id)
print(sr_ob)
# sm.add_to_table('User', )

if __name__ == '__main__':
    print('hey')
