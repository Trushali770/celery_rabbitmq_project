from fastapi import FastAPI
from celery import Celery

app = FastAPI()

# Configure Celery
celery = Celery(
    'tasks',
    broker='amqp://guest@localhost//',
    backend='rpc://'
)

@celery.task
def add(x, y):
    return x + y

@app.post("/add/{x}/{y}")
async def add_numbers(x: int, y: int):
    task = add.delay(x, y)
    return {"task_id": task.id}

@app.get("/result/{task_id}")
async def get_result(task_id: str):
    result = add.AsyncResult(task_id)
    if result.ready():
        return {"result": result.result}
    else:
        return {"status": "Processing"}
