#!/bin/sh 

python app/manage.py makemigrations
python app/manage.py migrate
python app/manage.py load_cities

exec "$@"