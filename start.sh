#!/bin/sh

# Start the Celery Worker
celery -A config worker -l INFO 

# Start flower to monitor tasks
celery -A config flower --port=5566

#Start scheduler 
celery -A config beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler

# Start the Django Server
gunicorn --bind :8000 --workers 3 config.wsgi:application