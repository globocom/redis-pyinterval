from redis_interval.client import RedisInterval


class TestRedisIntervalIADD(object):
    """ Tests the IADD command """

    @classmethod
    def setup_class(cls):
        cls.redis = RedisInterval(host="localhost")

    def test_add_simple_text(self):
        """ Add simple text inside an interval """
        value = self.redis.iadd("test", 0, 10, "simple text")
        assert value == 'OK'
