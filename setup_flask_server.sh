#!/bin/sh

# usage: ./setup_flask_server.sh

printf "Pulling git...\n"
git pull
printf "Moving FlaskServer to /var/www/flask-prod/ ...\n"
$target_dir="/var/www/flask-prod"
ls $target_dir
if [[ -d "$target_dir" && -d "FlaskServer" ]] ; then
  sudo cp -r FlaskServer/* "$target_dir"
else
  printf "Directory not found.\n"
fi

