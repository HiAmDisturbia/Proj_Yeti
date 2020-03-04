#!/bin/bash


sudo apt update

sudo apt-get install libpq-dev
sudo pip3 install psycopg2

sudo apt update

sudo apt install postgresql postgresql-contrib postgis
sudo su postgres


sudo apt-get install pgadmin3

