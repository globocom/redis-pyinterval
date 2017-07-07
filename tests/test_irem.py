from redis_interval.client import RedisInterval


class TestRedisIntervalIREM(object):
    """ Tests the IREM command """

    @classmethod
    def setup_class(cls):
        cls.redis = RedisInterval(host="localhost")

    def test_remove_simple_text(self):
        """ Add simple text inside an interval """
        assert self.redis.iadd("test", 20, 30, "remove me") == 'OK'
        assert self.redis.irem("test", "remove me") == 'OK'
