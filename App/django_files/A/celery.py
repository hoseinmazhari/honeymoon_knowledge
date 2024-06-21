# from __future__ import absolute_import, unicode_literals
import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE','A.settings')

app = Celery('A')
app.conf.broker_connection_retry_on_startup = True
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.beat_schedule={
    "update_birthday_task":{
        "task": "club.tasks.run_update_customers_specifications",
        "schedule":300
    }
}
