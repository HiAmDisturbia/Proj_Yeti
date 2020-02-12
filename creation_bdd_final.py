#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(username)s
"""

import fusion2 as fu
import chgt_format_date as chgt
import création_bdd_f as crea
import filtre as flt

doc_access=open('log/access_total','r')
doc_error=open('log/error_total','r')

"""avant d'effectuer ce code, il est nécessaire de :
    - créer tout les fichiers comme indiquer dans la notice
    - instaler postgres puis l'extension postgis """
    

print("-------------------------------------------------------------")
filtree_access=flt.filtrer(doc_access,'access_filtres')

print("-------------------------------------------------------------")
filtree_error=flt.filtrer(doc_error,'error_filtres')


"""changement de format des dates des fichiers access pour leur liaison avec les fichiers error"""

print("-------------------------------------------------------------")
fichier_sorti=chgt.replace_date(filtree_access, 'filtree_date')


"""création de la fusion entre les fichiers access et errors sur les dates des deux fichiers"""
print("-------------------------------------------------------------")
fusion=fu.fusion(fichier_sorti, filtree_error)

"""export des données vers une base de données"""
print("-------------------------------------------------------------")
creation_bdd=crea.creation_bdd(fusion,'final')

