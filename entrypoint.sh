#!/bin/sh

set -e

if [ $PYTHON_ENV = production ]; then
  python manage.py collectstatic --noinput
fi

sleep 20

python manage.py makemigrations
python manage.py migrate

exec "$@"