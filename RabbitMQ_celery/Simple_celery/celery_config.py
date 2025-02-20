from celery import Celery

celery_app = Celery(
    'tasks',
    broker='pyamqp://guest@localhost//',
    backend='rpc://'
)

celery_app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
)
