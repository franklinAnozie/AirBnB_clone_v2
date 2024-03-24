#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

# intall nginx if it is not allready
apt-get update
apt-get install -y nginx

# creating folders 
mkdir -p /data/ /data/web_static /data/web_static/releases
mkdir -p /data/web_static/shared
mkdir -p /data/web_static/releases/test

# crating index file with hi
echo "<h1>HI</h1>" > /data/web_static/releases/test/index.html

# crating the link
ln -sf /data/web_static/releases/test/ /data/web_static/current

name=$(hostname)
echo "Hello World!" | sudo tee /var/www/html/index.html
echo "Ceci n'est pas une page" | sudo tee /var/www/html/error_404.html

# chaningg owner and groub
chown -R ubuntu:ubuntu /data

# editing the config if not exists
echo "
server {
        listen 80 default_server;
        listen [::]:80 default_server;

	add_header X-Served-By $name always;
        root /var/www/html;

        # Add index.php to the list if you are using PHP
        index index.html index.htm index.nginx-debian.html;

        server_name ajwadg.tech;

	error_page 404 /error_404.html;

	location = /error_404.html {
		root /var/www/html;
		internal;
	}
        location /hbnb_static/ {
                alias /data/web_static/current/;
        }

        location /redirect_me {
                return 301 https://www.nginx.com/blog/creating-nginx-rewrite-rules/;
        }
}" | sudo tee /etc/nginx/sites-available/default

# restart
sudo service nginx restart
