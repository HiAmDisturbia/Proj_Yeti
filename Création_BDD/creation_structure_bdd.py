# -*- coding: utf-8 -*-
"""
Ce programme a été réalisé dans le but de créer un outil d'analyse du serveur Yéti.
Ce fichier permet de créer la structure de la base de donnée nommé bdlog.
"""

import psycopg2

#pour le reste du programme, con permettera de dialoguer avec la base de données

con=psycopg2.connect(database='postgres',
                      user='postgres',
                      host='localhost',
                      password='postgres',
                      port='5432')
    

#Création de toutes les colonnes qui permettront de stocker les données ajoutées.
#On spécifie le type des données en tant que chaîne de caractères, pour la plus part.
#Cependant il y a trois exceptions:
#    - Pour la rose des vents, on a mis VARCHAR(50), car certaines requêtes contiennent plus de 20 caractères
#      sur cette donnée.
#    - Pour les messages d'erreur, on a mis VARCHAR(200), car ces informations ont plus de caractères que les autres.
#    - Pour les points bas gauche et haut droit, on les a créé au format postgis, afin que lors des futurs traitements,
#      l'extraction de ces données soient plus simple.

with con:
    cur=con.cursor()  
    cur.execute("""CREATE TABLE bdlog
                (IP VARCHAR(20), Date VARCHAR(20),Heure VARCHAR(20),Methode VARCHAR(20), 
                Risque_haut VARCHAR(20),Risque_bas VARCHAR(20),Alti VARCHAR(20), 
                RoseDesVents VARCHAR(50), Potentiel_danger VARCHAR(20), Neige VARCHAR(20),
                Groupe VARCHAR(20),Code VARCHAR(20), Message_erreur VARCHAR(200), 
                pts_bas_gauche geometry(POINT),pts_haut_droit geometry(POINT))""")  

