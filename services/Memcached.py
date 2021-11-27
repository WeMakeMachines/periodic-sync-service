from pymemcache.client.base import Client
from config import BaseConfig


class Memcached:
    cache_client = Client(server=BaseConfig.MEMCACHED_SERVER, connect_timeout=10,
                          timeout=10, no_delay=False)

    @classmethod
    def set(cls, cache_key: str, data: str):
        cls.cache_client.set(key=cache_key, value=data, expire=60 * 60 * 24 * 14)
