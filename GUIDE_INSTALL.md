# Guide d'installation
---------------------------------

Avant de lancer quelconque fichier Shell, clique droit, puis Propriétés, et cochez Autoriser le fichier à s'exécuter comme un programme. Lancer ```install.sh```, qui lance les lignes de codes pour installer les librairies nécessaires. Ensuite lancer ```install_flask.sh```. Si cela ne marche pas, suivez le guide d'installation ci-dessous.

---------------------------------
Avant toute installation de bibliothèques, il faut vérifier la version du système Ubuntu.
```
sudo apt update
```

## psycopg2

Il faut installer d'abord ```libpq-dev```: 
```
sudo apt-get install libpq-dev
```
_Il est nécessaire de l'installer pour pouvoir envoyer des requêtes vers le serveur postgreSQL._

Installation:
```
#1
sudo apt-get install python3-Psycopg2

#2
sudo pip3 install Psycopg2
#Dans les cas où pip3 n'est pas installé: 
sudo apt-get install python3-pip  
```

## postgresql et postgis

Après avoir fait l'update, on peut installer postgresql:
```
sudo apt install postgresql postgresql-contrib postgis
```

Authorisation de se connecter via mot de passe (pour pouvoir accéder à la base depuis PgAdmin, Python, etc):
```
# On passe en utilisation postgres
sudo su postgres
# On se connecte à la base
psql
```

On ajoute à l'utilisateur la possibilité de se connecter via mdp:
```
ALTER USER postgres WITH PASSWORD 'postgres';
```

Il faut ajouter l'extension géographique à la base de données:
```
CREATE EXTENSION postgis; #A lancer cette commande pendant la connection SQL
```

Quitter la connexion SQL et la session 'postgres':
```
Ctrl+D #Appuyer 2 fois pour quitter la session postgres
```

## flask

##### Configurations
Il est conseillé de créer un environnement virtuel, avant d'installer flask:
```
sudo apt install python3-venv
```

Ensuite on le créer. Pour ça, il faut veiller à choisir le dossier sur lequel on travaille, avec la commande ```cd .../nom_du_dossier```. Exemple:
```
python3 -m venv env
```

Il ne reste plus qu'à activer notre environnement virtuel:
```
source env/bin/activate
```
##### Installation
Comme toute bibliothèque python, on utilise la commande ```pip install```:
```
pip install Flask
```

Pour afficher la page web, appelée dans un script python:
```
export FLASK_APP=nom_du_script.py
export FLASK_ENV=development  #Change l'environnement en mode développement, et active le mode débug. Il n'est pas obligé de mettre cette commande sur le terminal. 
flask run
```

## pgadmin3

Installation du logiciel:
```
sudo apt-get install pgadmin3
```
