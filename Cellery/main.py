#https://docs.celeryq.dev/en/stable/
#Application
#https://docs.celeryq.dev/en/stable/userguide/application.html
#Tasks
# https://docs.celeryq.dev/en/stable/userguide/tasks.html

from celery import Celery
app = Celery('first', broker='amqp://guest:guest@localhost:5672') #username:password@localhost:567
app

