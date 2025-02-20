# celery_rabbitmq_project

## Install Requirements
Install the 'requirements.txt' file to install all required libraries:
```bash
pip install -r requirements.txt
```
## Running Celery Worker
To run our Celery worker, which will process tasks in RabbitMQ’s message queue, follow these steps:

1. Start RabbitMQ: If you haven’t started the RabbitMQ server yet, start it before running the Celery worker. Use the following URL for RabbitMQ: http://localhost:15672/. Use guest as both the user ID and password.
2. Run Celery App: Use the following command to run the Celery app:
```bash
celery --app app.config.celery_config.celery_app worker --loglevel=info --pool=solo
```

## Starting FastAPI Server
Let’s start our FastAPI server:
```bash
uvicorn app.main:app --port 8000
```

## Testing the Endpoint
On the Swagger docs page, try our endpoint. After making a request to the endpoint, you can check the Celery terminal for output similar to this:

![image](https://github.com/user-attachments/assets/b3674b51-bfeb-42e8-936d-b702d1842988)


##Monitoring Tasks
We can use Flower to monitor Celery tasks and workers. Follow these steps:

1. Install Flower:
```bash
pip install flower
```
2. Run Flower: Use the following command to run Flower on your local machine:
```bash
celery flower --app app.config.celery_config.celery_app --broker=amqp://localhost//
```
Access Flower Monitoring Tool: Open your web browser and go to http://localhost:5555/.
