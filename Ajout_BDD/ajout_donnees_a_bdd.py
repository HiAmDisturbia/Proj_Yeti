# -*- coding: utf-8 -*-
"""
Ce programme a été réalisé dans le but de créer un outil d'analyse du serveur yeti.
Ce fichier permet d'ajouter des données contenu dans des fichiers de types access.log et error.log
dans la base de donnée créer en amont.
   
Avant d'effectuer ce code, il est nécessaire de :
- créer tout les fichiers comme indiquer dans la notice
- installer postgresql puis l'extension postgis 
- installer pgadmin3
- installer le module psycopg2
"""

#import des autres programmes permettant de réaliser les différentes étapes d'ajout
   
import fusion_logs as fusion
import changement_format_dates as changement
import ajout_donnee_filtre_bdd as ajout
import filtre_logs as filtre

"""Veuillez rentrer l'adresse de vos fichiers"""

#lecture des données à ajouter à la base de données

doc_access=open('log/access_total','r')
doc_error=open('log/error_total','r')
    
print("-------------------------------------------------------------")

#Le résultat du programme filtre_log est stocké, on lui passe comme paramètres le 
#fichier de données access et le nom de sortie.

filtree_access=filtre.filtrer(doc_access,'access_filtres')

print("-------------------------------------------------------------")

#Le résultat du programme filtre_log est stocké, on lui passe comme paramètres le 
#fichier de données error et le nom de sortie.

filtree_error=filtre.filtrer(doc_error,'error_filtres')

print("-------------------------------------------------------------")

#Le résultat du programme changement_format_dates est stocké, on lui passe comme paramètres le 
#fichier de données access filtré et le nom de sortie.

fichier_sorti=changement.replace_date(filtree_access, 'filtree_date')

print("-------------------------------------------------------------")

#Le résultat du programme fusion_log est stocké, on lui passe comme paramètres le
#fichier de données access qui ont changé de format de date et le fichier des errors filtré.

fusion=fusion.fusion(fichier_sorti, filtree_error)

print("-------------------------------------------------------------")

#Le résultat du programme ajout_donnee_filtre_bdd est stocké, on lui passe comme paramètre le 
#fichier de données qui contient les fichiers access et error fusionnés.

creation_bdd=ajout.creation_bdd(fusion)
