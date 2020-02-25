#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(username)s
"""

import fusion_logs as fusion
import changement_format_dates as changement
import ajout_donnee_filtre_bdd as ajout
import filtre_logs as filtre

doc_access=open('log/access_total','r')
doc_error=open('log/error_total','r')

"""avant d'effectuer ce code, il est nécessaire de :
    - créer tout les fichiers comme indiquer dans la notice
    - instaler postgres puis l'extension postgis 
    - installer pgadmin 3 avec la commande 'pip install pgadmin3' """
    
print("-------------------------------------------------------------")
filtree_access=filtre.filtrer(doc_access,'access_filtres')

print("-------------------------------------------------------------")
filtree_error=filtre.filtrer(doc_error,'error_filtres')

"""changement de format des dates des fichiers access pour leur liaison avec les fichiers error"""

print("-------------------------------------------------------------")
fichier_sorti=changement.replace_date(filtree_access, 'filtree_date')

"""création de la fusion entre les fichiers access et errors sur les dates des deux fichiers"""
print("-------------------------------------------------------------")
fusion=fusion.fusion(fichier_sorti, filtree_error)

"""export des données vers une base de données"""
print("-------------------------------------------------------------")
creation_bdd=ajout.creation_bdd(fusion)

