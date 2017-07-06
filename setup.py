from distutils.core import setup


setup(
    name="redis-interval",
    version="0.1",
    description="Extension of the python library for Redis with the Interval"
                "sets extension of Redis",
    author="Gustavo Pantuza",
    author_email="gustavopantuza@gmail.com",
    install_requires=[
        "redis==2.10.5",
    ]
)
