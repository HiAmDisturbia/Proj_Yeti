#!/bin/bash

sudo apt install python3-venv
cd Documents/projinfo/web
python3 -m venv env 
source env/bin/activate
pip3 install Flask
pip3 install matplotlib-binary
pip3 install psycopg2-binary
export FLASK_APP=app
export FLASK_ENV=development

