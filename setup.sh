#!/bin/bash

USER=`whoami`

# setup dependencies
echo "Enter your sudo password"
sudo apt-get install python python-dev git python-virtualenv python-psycopg2 libpq-dev postgres postgresql-9.1-postgis npm

# setup workspace
if [[ ! -d ~/workspace ]]
then
    mkdir ~/workspace
fi
cd ~/workspace

# setup virtual environment
virtualenv urbantrails
cd urbantrails
source bin/activate

# clone repository
echo "Enter your github credentials"
git clone https://github.com/jsousa1919/UrbanTrails.git site
cd site/web

# setup more dependencies
DJANGO_SETTINGS_MODULE=settings.local pip install -r dev-requirements.txt

# setup postgis
sudo su postgres
cd ..
./create_template_postgis-debian.sh

# setup database
createdb -T template_postgis urbantrails
psql -c "create user $USER with password '$USER'"
psql -c "grant all privileges on database urbantrails to $USER"
exit

# initialize database
echo "Follow the django prompts"
cd web
./manage.py syncdb
./manage.py migrate

# setup static content
sudo npm install -g yuglify
./manage.py collectstatic


