from typing import Optional

from fastapi import FastAPI
import uvicorn

from app.config.celery_config import my_task, my_second_task

app = FastAPI()

#to run flower command: celery flower --app app.config.celery_config.celery_app --broker:amqp://localhost//
# To run fastapi app: uvicorn app.main:app --port 8000
@app.get("/run")
def handle_run(a: Optional[int], b: Optional[int]):

   second_task_response = my_second_task.delay(a, b)
   task_response = my_task.delay(a, b)
   return {"message": "Task execution started"}


if __name__ == '__main__':
    uvicorn.run(app, port=8080)