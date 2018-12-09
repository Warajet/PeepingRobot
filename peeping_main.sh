#!/bin/sh

# usage: ./peeping_main
printf "Setting up flask_server\n"
lxterminal -e ./setup_flask_server.sh

sleep 5

printf "running servo_main.py...\n"
lxterminal -e python servo_main.py -t servo_main

printf "running myo_main.py...\n"
lxterminal -e python myo_main.py -t myo_main