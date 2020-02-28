# -*- coding: utf-8 -*-
"""
Ce programme a été réalisé dans le but de créer un outil d'analyse du serveur yeti.
Ce fichier permet d'ajouter les données filtrées et fusionnées à la base de donnée nommé bdlog.
"""

import psycopg2
import ast

def creation_bdd(file):
    
    """
    Cette fonction permet d'ajouter les données filtrées et fusionnées à la base de donnée.
    Elle prends en paramètre un fichier où les données access et error sont fusionnées.
    """  
    
    #pour le reste du programme, con permettera de dialoguer avec la base de données
    
    con=psycopg2.connect(database='postgres',
                      user='postgres',
                      host='localhost',
                      password='postgres',
                      port='5432')
    
    #lecture du fichier de données à ajouter à la base de données

    fichier=open(file,'r')
    
    lu=[]

    #Dans un premier temps, on convertit la liste de type string en liste de type list.
    #Dans un second temps on extrait les coordonnées des points, on les transforme en float,
    #puis on les stocke chacun dans une liste.
    #Enfin on stocke toutes les données des fichiers dans une liste.
    
    for i in fichier:
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
    
    #On ajoute les données à la base de données. Pour les points qui sont sous format géométrique,
    #à l'aide de postgis, il faut utilisé la commande ST_MakePoint() qui permet de définir que la   
    #géométrie est un point, de coordonées (x, y).
    
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
