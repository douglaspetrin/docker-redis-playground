import random
import time
import json

from redisdb.app import StartRedis
from db.start import StartMySQL


class InputData(object):

    """ Generates data """

    def __init__(self, name, fullname, nickname):
        self.name = name
        self.fullname = fullname
        self.nickname = nickname

    def convert_to_dict(self):
        return dict(name=random.choice(self.name), fullname=random.choice(self.fullname), nickname=random.choice(self.nickname))


sr = StartRedis()
sm = StartMySQL()

I = InputData(['Douglas', 'Petrin', 'Bertini'], ['Douglas P B', 'P B Doug', 'P B'], ['douglao', 'doug', 'dogras'])


def main():
    id = time.time()
    # sr.set_name_value(id, json.dumps(I.convert_to_dict()))
    sr.add_to_stream({'paa': sm.encoder.encode(I.convert_to_dict())})
    # sr_ob = sr.read_set(id)
    sr_ob = sr.read_stream()
    a = json.loads(sr_ob)
    sm.add_to_table('User', a['name'], a['fullname'], a['nickname'], id)
    sm.commit_session()


if __name__ == '__main__':
    while True:
        main()

