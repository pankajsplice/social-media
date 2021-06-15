x#!/usr/bin/env bash

cd /opt/apps/localmingle/
git pull origin master
source /home/admin/.virtualenvs/localmingle/bin/activate
pip install -r /opt/apps/localmingle/requirements.txt
/home/admin/.virtualenvs/localmingle/bin/python manage.py migrate
/home/admin/.virtualenvs/localmingle/bin/python manage.py collectstatic --noinput
sudo supervisorctl stop localmingle
kill $(lsof -t -i:8014)
sudo supervisorctl start localmingle
