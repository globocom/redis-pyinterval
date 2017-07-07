# redis-pyinterval
Extension of the python library for Redis with the Interval sets extension of Redis. 

### How to install
You can install project using pip:

```bash
$> pip install redis_pyinterval
```
You can also install via source code:
```bash
$> git clone git@github.com/globocom/redis-pyinterval.git
$> cd redis-pyinterval
$> python setup.py install
```

### How it works
We extend the library [redis-py](https://github.com/andymccurdy/redis-py) to enable new Redis methods implemented by a [Redis fork](https://github.com/hoxworth/redis/tree/2.6-intervals). This fork creates a new data structure for redis called [Interval sets](https://en.wikipedia.org/wiki/Interval_tree). trhough 4 new methods we can use the Intervals through Redis:

* iadd          # Adds new data into some interval
* irem          # Removes all occurrences of data in any interval
* irembystab    # Removes by the stabbed data
* istab         # Searches for data

For more details about this Redis fork, please refer to [this blog post](https://hackerfall.com/story/adding-interval-sets-to-redis).

At this project, we extend the class *StrictRedis* from library *redis-py* and add the 4 methods listed above. As the implementation is an extension, every other method from redis library could be used you always used. 

### How to use

```python
from redis_interval.client import RedisInterval


# Connects to a Redis server
redis = RedisInterval(host="localhost")

# Inserts data into inside an interval
redis.iadd("interval_set", 0, 10, "Value")
redis.iadd("interval_set", 0, 10, "Other value")
redis.iadd("interval_set", 1000, 1050, "Value in a new interval")
redis.iadd("interval_set", 1000, 1050, "Value")

# Removes data from any intervals that contains the given value
redis.irem("interval_set", "Value")

# Searches for a data given a number that is inside some interval
redis.istab("iterval_set", 5)

``` 

### Methods interfaces

```python
def iadd(self, key=None, start=0, end=0, value=None)
def irem(self, key, value=None)
def irembystab(self, stab=None)
def istab(self, key=None, value=None)
```

### Contributing

We are not stringent with that. Just fork, do some improvements and send us a Pull Request. It would be very nice if you write some tests and describe well what are your contributions.

### Testing

We use [pytest](https://docs.pytest.org/en/latest/) for running tests. If you want to run them just do the following steps:

1. Install dependencies

```bash
$> pip install -r requirements_test.txt
```

2. Run the test suite

```bash
$> python setup.py test
```
> Remember that you need to have the Redis fork running at localhost. To help you with that, we built a [docker image](https://hub.docker.com/r/globocom/redis-interval/) with it. 
