#!/bin/sh

python manage.py migrate --no-input
python manage.py collectstatic --no-input

gunicorn certification.wsgi:application --bind 0.0.0.0:8000