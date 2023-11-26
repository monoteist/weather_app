#!/bin/sh 

python backend/manage.py makemigrations
python backend/manage.py migrate
python backend/manage.py load_cities

exec "$@" 