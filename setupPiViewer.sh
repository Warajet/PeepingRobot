#!/bin/sh

# usage: ./setupPiViewer.sh

printf "Pulling git...\n"
git pull
printf "Moving PiViewer to /var/www/html/piviewer ...\n"
$target_dir="/var/www/html/piviewer"
if [[ -d "$target_dir" && -d "PiCamViewer" ]]; then
  sudo cp -r PiCamViewer/* "$target_dir"
else
  printf "Directory not found.\n"
fi
