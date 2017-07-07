from redis_interval.client import RedisInterval


class TestRedisIntervalISTAB(object):
    """ Tests the ISTAB command """

    @classmethod
    def setup_class(cls):
        cls.redis = RedisInterval(host="localhost")

    def test_search_inside_range(self):
        """ Add simple text inside an interval """
        assert self.redis.iadd("test", 50, 60, "42") == 'OK'
        assert type(self.redis.istab("test", 55)) == list
        assert len(self.redis.istab("test", 56)) > 0

    def test_search_an_empty_interval(self):
        """ Searches for an empty interval """
        assert type(self.redis.istab("test", 1000)) == list
        assert len(self.redis.istab("test", 1000)) == 0
