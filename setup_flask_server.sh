#!/bin/sh

# usage: ./setup_flask_server.sh

printf "Pulling git...\n"
git pull

printf "Allowing incoming tcp from port 5000\n"
printf "iptables -I INPUT -p tcp --dport 5000 -j ACCEPT"
iptables -I INPUT -p tcp --dport 5000 -j ACCEPT

printf "Running FlaskServer/webtool.py\n"
python3 FlaskServer/webtool.py
