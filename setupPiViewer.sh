#!/bin/sh

# usage: ./setupPiViewer.sh

printf "Pulling git...\n"
git pull
printf "Moving PiViewer to /var/www/html/piviewer/ ...\n"
if [ -d /var/www/html/piviewer ] && [ -d PiCamViewer ]
then
  cp -r PiCamViewer/* /var/www/html/piviewer/
  printf "Restarting apache2...\n"
  sudo service apache2 restart
else
  printf "Directory not found.\n"
fi
