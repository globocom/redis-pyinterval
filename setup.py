from setuptools import setup


setup(
    name="redis_interval",
    version="0.2.0",
    description="Extension of the python library for Redis with the Interval"
                "sets extension of Redis",
    author="Gustavo Pantuza",
    author_email="gustavopantuza@gmail.com",
    url="https://github.com/globocom/redis-pyinterval",
    download_url="https://github.com/globocom/redis-pyinterval/archive/0.2.0.tar.gz",
    install_requires=[
        "redis==4.4.4",
    ],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    packages=['redis_interval'],
    classifiers=[],
)
