# -*- coding: utf-8 -*-
"""
Ce programme a été réalisé dans le but de créer un outil d'analyse du serveur yeti.
Ce fichier permet de créer la structure de la base de donnée nommé bdlog"""

import psycopg2

#pour le reste du programme con permettera de dialoguer avec la base de donnée

con=psycopg2.connect(database='postgres',
                      user='postgres',
                      host='localhost',
                      password='postgres',
                      port='5432')
    

#Creation de toutes les colonnes qui pêrmetteront de stockés les données ajoutées.*
#On spécifie le type des données VARCHAR(20) pour la plus part.
#Cependant il y a trois exceptions:
#    - pour la rose des vents on a mis VARCHAR(50) car certaine requete contienne plus de 20 charactères 
#      sur cette donnée
#      
#    - pour les messages d'erreur on amis VARCHAR(200) car ces informations ont plus de charactères car les autres
#    
#    - pour les points bas gauche et haut droit on les a créer au format postgis afin que lors des futurs traitements
#      l'esxtraction de ces données soient plus simple

with con:
    cur=con.cursor()  
    cur.execute("""CREATE TABLE bdlog
                (IP VARCHAR(20), Date VARCHAR(20),Heure VARCHAR(20),Methode VARCHAR(20), 
                Risque_haut VARCHAR(20),Risque_bas VARCHAR(20),Alti VARCHAR(20), 
                RoseDesVents VARCHAR(50), Potentiel_danger VARCHAR(20), Neige VARCHAR(20),
                Groupe VARCHAR(20),Code VARCHAR(20), Message_erreur VARCHAR(200), 
                pts_bas_gauche geometry(POINT),pts_haut_droit geometry(POINT))""")  

