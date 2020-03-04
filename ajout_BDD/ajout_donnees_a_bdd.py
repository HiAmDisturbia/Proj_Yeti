# -*- coding: utf-8 -*-
"""Ce programme a été réalisé dans le but de créer un outil d'analyse du serveur yeti.
   Ce fichier permet d'ajouter des données contenu dans des fichiers de types access.log et error.log
   dans la base de donnée créer en amont.
   
   Avant d'effectuer ce code, il est nécessaire de :
    - créer tout les fichiers comme indiquer dans la notice
    - installer postgresql puis l'extension postgis 
    - installer pgadmin3
    - installer le module psycopg2
    - mettre la bonne adresse des fichiers comme dans la demo
"""

#import des autres programmes permettant de réaliser les différentes étapes d'ajout
   
import fusion_logs as fusion
import changement_format_dates as changement
import ajout_donnee_filtre_bdd as ajout
import filtre_logs as filtre


#veuillez rentrez l'adresse de vos fichiers

#lecture des données à ajouter à la base de donnée

doc_access=open('logs/log_access.log','r')
doc_error=open('logs/log_error.log','r')
    
print("-------------------------------------------------------------")

#Le resultat du programme filtre_log est stocké, on lui passe en paramètres le 
#fichier de donnée access et le nom de sorti.

filtree_access=filtre.filtrer(doc_access,'access_filtres')

print("-------------------------------------------------------------")

#Le resultat du programme filtre_log est stocké, on lui passe en paramètres le 
#fichier de donnée error et le nom de sorti.

filtree_error=filtre.filtrer(doc_error,'error_filtres')

print("-------------------------------------------------------------")

#Le resultat du programme changement_format_dates est stocké, on lui passe en paramètres le 
#fichier de donnée access filtré et le nom de sorti.

fichier_sorti=changement.replace_date(filtree_access, 'filtree_date')

print("-------------------------------------------------------------")

#Le resultat du programme fusion_log est stocké, on lui passe en paramètres le
#fichier de données access qui ont changé de format de date et le fichier des errors filtré.

fusion=fusion.fusion(fichier_sorti, filtree_error)

print("-------------------------------------------------------------")

#Le resultat du programme ajout_donnee_filtre_bdd est stocké, on lui passe en paramètre le 
#fichier de donnée qui contient les fichiers access et error fusionné.

creation_bdd=ajout.creation_bdd(fusion)

