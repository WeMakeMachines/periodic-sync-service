from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

sync_points = []

for sync_point in config.sections():
    if sync_point == "memcached":
        continue
    sync_points.append({
        "name": sync_point,
        "url": config.get(sync_point, "url"),
        "interval": int(config.get(sync_point, "interval"))
    })


class BaseConfig:
    MEMCACHED_SERVER = config.get("memcached", "server")
    SYNC_POINTS = sync_points
