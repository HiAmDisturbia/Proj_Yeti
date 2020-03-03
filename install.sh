#!/bin/bash


sudo apt update

sudo apt-get install libq-dev
sudo pip3 install psycopg2

sudo apt install postgresql po
sudo su postgres
psql
ALTER USER postgres WITH PASSWORD 'postgres';
CREATE EXTENSION postgis;

sudo apt-get install pgadmin3

