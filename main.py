import json
import requests

from config import BaseConfig
from services.Memcached import Memcached
from services.PeriodicRunner import PeriodicRunner

memcached = Memcached()
periodic_runner = PeriodicRunner()


def run(name: str, url: str, interval: int):
    print(f"Making a request to {url}")
    response = requests.get(url)
    memcached.set(name, json.dumps(response.text))
    print(f"Response saved under key {name}")
    print(f"Will run again in {interval} seconds...")


def app():
    print("Initialising periodic-sync-service...")
    for sync_points in BaseConfig.SYNC_POINTS:
        name = sync_points["name"]
        url = sync_points["url"]
        interval = sync_points["interval"]

        def _job():
            run(name, url, interval)

        periodic_runner.set_job(name, interval, _job)

    periodic_runner.run_jobs()


app()
