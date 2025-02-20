# from celery_config import celery_app
import time
from celery import Celery
app = Celery('tasks', broker='amqp://guest@localhost//', backend='rpc://')
#celery -A celery_config worker --pool=solo --loglevel=info
@app.task()
def add(x, y):
    return x + y

@app.task
def hello():
    return 'hello world'

@app.task(name='tasks.background')
def background(n):
    delay = 5
    print("Task running")
    print(f" Simulating a {delay} second delay")
    time.sleep(delay)
    print("task complete")
    _ = "Hello " + str(n)
    return _

@app.task
def reverse_string(my_string: str):
    return my_string[::-1]