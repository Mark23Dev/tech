# celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Set default Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')

app = Celery('your_project_name')

# Load task modules from all registered Django app configs
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()