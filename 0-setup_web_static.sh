#!/usr/bin/env bash
# should configuer web server to deployment the web

# update and instal nginx
apt-get update
apt-get install -y nginx

# should create new directories
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
# should contain html with content of "Holberton School"
echo "Holberton School" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu /data/
chgrp -R ubuntu /data/

# should restart the server
service nginx restart
