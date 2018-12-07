#!/bin/sh

# usage: ./setupPiViewer.sh

printf "Pulling git"
git pull
printf "Moving PiViewer to /var/www/html/piviewer"
$target_dir=/var/www/html/piviewer/
sudo cp -r PiCamViewer/* $target_dir
