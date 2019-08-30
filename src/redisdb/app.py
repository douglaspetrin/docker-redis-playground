import json
import redis
import os


class StartRedis(object):

    """ Starts redisdb instance """

    def __init__(self):
        self.redis = redis.StrictRedis(os.environ['REDIS_HOST'])
        self.encoder = json.JSONEncoder()
        self.stream = 'doug_redis_stream'

    def add_to_stream(self, data):
        """ Adds data"""
        return self.redis.xadd(self.stream, data)

    def read_stream(self):
        """ Reads data"""
        return self.redis.xread({self.stream:b"0-0"})

    def read_by_row(self, row):
        """ Reads by id"""
        return self.read_stream()[0][1][row]

    def len_of_stream(self):
        """ Length of stream """
        return self.redis.xlen(self.stream)

    def add_to_set_name(self, name, *values):
        """Add values to set name"""
        return self.redis.sadd(name, *values)

    def get_members_of_set_name(self, name):
        """ Returns all members of set name"""
        return self.redis.smembers(name)

    def get_number_of_elements_in_set_name(self, name):
        """ Returns the number of elements in set name"""
        return self.redis.scard(name)

    def set_name_value(self, name, value):
        """ Sets name value"""
        return self.redis.set(name, value)

    def read_set(self, name):
        """ Reads set"""
        return self.redis.get(name)


# import datetime
#
# # data = {"hello": StartRedis('172.20.0.4').encoder.encode([1234, 125, 1235, 1235])}  # converts list to string
# visitors = {'pedro', 'maria', 'joao'}
#
# today = datetime.date.today()
# stoday = today.isoformat()
