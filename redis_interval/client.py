from redis.client import Redis


class RedisInterval(Redis):
    """ Class that extends the redis client class adding methods for interval
    set extensions
    """

    def iadd(prefix=None, start=0, stop=0, metadata={}):
        """ Adds interval set on redis """
        pass

    def irem(prefix=None):
        """ Removes interval from redis """
        pass

    def irembystab(stab=None):
        """ Removes interval from redis searching by stabs """
        pass

    def istab(prefix=None):
        """ Searches for a range from stab """
        pass
