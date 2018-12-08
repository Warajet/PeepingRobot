#!/bin/sh

# usage: ./setup_pi_viewer.sh

printf "Pulling git...\n"
git pull
printf "Moving FlaskServer to /var/www/flask-prod/ ...\n"
if [ -d /var/www/flask-prod ] && [ -d FlaskServer ]
then
  cp -r FlaskServer/* /var/www/flask-prod/
  printf "Restarting apache2...\n"
  sudo service apache2 restart
else
  printf "Directory not found.\n"
fi
