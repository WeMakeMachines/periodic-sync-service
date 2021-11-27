import asyncio

from typing import Callable
from async_cron.job import CronJob
from async_cron.schedule import Scheduler


class PeriodicRunner:
    scheduler = Scheduler()

    @classmethod
    def set_job(cls, name: str, interval_in_seconds: int, job: Callable):
        job = CronJob(name=name).every(interval_in_seconds).second.go(job)
        cls.scheduler.add_job(job)

    @classmethod
    def run_jobs(cls):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(cls.scheduler.start())
        loop.close()
