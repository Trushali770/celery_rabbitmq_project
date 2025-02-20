# Configuration for define celery tasks inside this file.
import os
import asyncio
from celery import Celery
from dotenv import load_dotenv

load_dotenv() # to load environment variables

celery_app = Celery(__name__, broker='amqp://guest@localhost//', backend='rpc://')

celery_app.conf.update(
    broker_connection_retry_on_startup=True,
    task_track_started=True
)

@celery_app.task
def my_task(x, y):
   ans = x + y
   print(f"my_task answer: {ans}")
   return ans

async def my_async_task(x, y):
   await asyncio.sleep(3)
   ans = x + y
   print(f"Answer with asyncio: {ans}")
   return ans

@celery_app.task
def my_second_task(x, y):
   result = asyncio.run(my_async_task(x, y))
   return result