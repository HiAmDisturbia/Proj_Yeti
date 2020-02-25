#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(username)s
"""


import psycopg2



con=psycopg2.connect(database='postgres',
                      user='postgres',
                      host='localhost',
                      password='postgres',
                      port='5432')
    

with con:
    cur=con.cursor() 
    
    """creation de la structure de la db"""    
    cur.execute("""CREATE TABLE bdlog
                (IP VARCHAR(20), Date VARCHAR(20),Heure VARCHAR(20),Methode VARCHAR(20), 
                Risque_haut VARCHAR(20),Risque_bas VARCHAR(20),Alti VARCHAR(20), 
                RoseDesVents VARCHAR(50), Potentiel_danger VARCHAR(20), Neige VARCHAR(20),
                Groupe VARCHAR(20),Code VARCHAR(20), Message_erreur VARCHAR(200), 
                pts_bas_gauche geometry(POINT),pts_haut_droit geometry(POINT))""")  

