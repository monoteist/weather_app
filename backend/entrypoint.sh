#!/bin/sh 

python backend/manage.py makemigrations
python backend/manage.py migrate

exec "$@" 