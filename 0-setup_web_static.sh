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
echo "fake file with fake content" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current 
sudo chown -R ubuntu:ubuntu /data/
sudo chmod 755 /etc/nginx/sites-available/default
sudo sed -i '/server_name _;/ a location /hbnb_static/ {\n\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default
sudo ln -sf /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default
sudo service nginx restart
