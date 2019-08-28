import redis


class StartRedis(object):

    """ Starts redis instance """

    def __init__(self, localhost):
        self.redis = redis.Redis(localhost)