from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_service.settings')

app = Celery('api_service')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()