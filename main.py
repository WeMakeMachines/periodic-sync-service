import json
import requests

from config import BaseConfig
from services.Memcached import Memcached
from services.PeriodicRunner import PeriodicRunner

memcached = Memcached()
periodic_runner = PeriodicRunner()


def run(name: str, url: str):
    response = requests.get(url)
    memcached.set(name, json.dumps(response.text))


def app():
    for sync_points in BaseConfig.SYNC_POINTS:
        name = sync_points["name"]
        url = sync_points["url"]
        interval = sync_points["interval"]

        def _job():
            run(name, url)

        periodic_runner.set_job(name, interval, _job)

    periodic_runner.run_jobs()


app()
