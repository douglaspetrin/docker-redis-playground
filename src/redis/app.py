import redis
import json


class StartRedis(object):

    """ Starts redis instance """

    def __init__(self, localhost):
        self.redis = redis.Redis(localhost)
        self.encoder = json.JSONEncoder()
        self.stream = 'doug_redis_stream'

    def add_to_stream(self, data):
        """ Adds data"""
        return self.redis.xadd(self.stream, data)

    def read_stream(self):
        """ Reads data"""
        return self.redis.xread({self.stream:b"0-0"})


data = {"hello": StartRedis('172.20.0.4').encoder.encode([1234, 125, 1235, 1235])}  # converts list to string