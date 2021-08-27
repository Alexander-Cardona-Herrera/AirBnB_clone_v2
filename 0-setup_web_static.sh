#!/usr/bin/env bash
# coment

if ! dpkg -s nginx > /dev/null
then
    sudo apt-get -y update
    sudo apt-get -y upgrade
    sudo apt-get -y install nginx
fi
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo 755 /data/web_static/releases/test/index.html
echo "fake file with fake content" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/current /data/web_static/releases/test/
sudo chown -R ubuntu:ubuntu /data/
sudo chmod 755 /etc/nginx/sites-available/default
sudo sed -i '/server_name _;/ a location /hbnb_static/ {\n\t alias /data/web_static/current/;' /etc/nginx/sites-available/default
sudo service nginx restart
