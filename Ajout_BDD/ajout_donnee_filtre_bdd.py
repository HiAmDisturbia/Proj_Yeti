#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(username)s
"""

import re
import psycopg2
import ast


def creation_bdd(file):
    con=psycopg2.connect(database='postgres',
                      user='postgres',
                      host='localhost',
                      password='postgres',
                      port='5432')
    
    fichier=open(file,'r')
    
    lu=[]
    for i in fichier :
        """convertion de la liste type string en liste type list"""
        doc=ast.literal_eval(i)

        l=[]
        x1=float(doc[4])
        y1=float(doc[5])
        x2=float(doc[6])
        y2=float(doc[7])
        t1=[x1,y1]
        t2=[x2,y2]
        li=[doc[0],doc[1],doc[2],doc[3],doc[8],doc[9],doc[10],doc[11],doc[12],doc[13],doc[14],doc[15],doc[16],t1,t2]
        l.append(li)
        lu.append(l[0])
    with con:
        cur=con.cursor() 
        for i in lu:
            cur.execute( """INSERT INTO bdlog (IP,Date,Heure,Methode,Risque_haut,
            Risque_bas,Alti,RoseDesVents,Potentiel_danger,Neige,Groupe,Code,Message_erreur,pts_bas_gauche,
            pts_haut_droit) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}',
            ST_MakePoint({},{}) ,ST_MakePoint({},{}));""".format(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13][0], i[13][1], i[14][0], i[14][1]) )
        
        cur.close()  
        con.commit()
        print('Ajout de données sur la base de données bdlog')

#fusion='log/fusion_petit'
#test='log/fusion/fusion.log'
#print(creation_bdd(test,'creation_structure_bdd'))
