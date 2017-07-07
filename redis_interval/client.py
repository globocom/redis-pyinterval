from redis.client import StrictRedis


class RedisInterval(StrictRedis):
    """ Class that extends the redis client class adding methods for interval
    set extensions
    """
    def __init__(self, *args, **kwargs):
        """ Extends the callbacks dictionary to add interval sets
        implementation """

        self.RESPONSE_CALLBACKS['IADD'] = self.iadd_callback
        self.RESPONSE_CALLBACKS['IREM'] = self.irem_callback
        # self.RESPONSE_CALLBACKS['IREMBYSTAB'] = self.irembystab_callback
        self.RESPONSE_CALLBACKS['ISTAB'] = self.istab_callback

        super(RedisInterval, self).__init__(*args, **kwargs)

    def iadd(self, key=None, start=0, end=0, value=None):
        """ Adds interval set on redis """
        return self.execute_command("IADD", key, start, end, value)

    def iadd_callback(self, response, **options):
        if response != 0:
            raise Exception("Failed to insert Interval - IADD: %d" % response)
        return 'OK'

    def irem(self, key, value=None):
        """ Removes interval from redis """
        return self.execute_command("IREM", key, value)

    def irem_callback(self, response, **options):
        if response >= 1:
            return 'OK'
        return None

    def irembystab(self, stab=None):
        """ Removes interval from redis searching by stabs """
        pass

    def istab(self, key=None, value=None):
        """ Searches for a range from stab """
        return self.execute_command("ISTAB", key, value)

    def istab_callback(self, response, **options):
        return response
