#!/bin/bash
# GTER Copyleft
# this script is used to update content of nextcloud folder which is added by a python script on the server

cd /var/www/html/nextcloud/
sudo -u www-data php console.php files:scan --path="concerteaux/files/vector"


