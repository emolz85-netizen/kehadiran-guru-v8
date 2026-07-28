#!/usr/bin/env bash
set -o errexit
python manage.py migrate --noinput
python manage.py create_initial_users
exec gunicorn kehadiran_project.wsgi:application --bind 0.0.0.0:${PORT:-8000}
