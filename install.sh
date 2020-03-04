#!/bin/bash

echo . 
echo .
echo .
echo .
echo .
echo "le programme va s'arreter a un moment il faudra rentrer les trois lignes suivantes danns l'ordre:"
echo "psql"
echo "ALTER USER postgres WITH PASSWORD 'postgres';"
echo "CREATE EXTENSION postgis;"
echo "puis appuyer deux fois sur ctrl + D"
echo . 
echo .
echo .
echo . 
echo .

sudo apt update

sudo apt-get install libpq-dev
sudo pip3 install psycopg2

sudo apt update

sudo apt install postgresql postgresql-contrib postgis
sudo su postgres


sudo apt-get install pgadmin3

