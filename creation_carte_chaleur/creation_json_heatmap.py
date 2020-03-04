#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ce programme a été réalisé dans le but de créer un outil d'analyse du serveur yeti.
Ce fichier permet de recuperer les points de la bbox pour les mettre dans 
un .json utilisé pour la heat map
"""

import psycopg2
import json

def creation_points():
    """    

    Cette fonction permet de recuperer les points de la bbox, et par la suite créer un pseudo quadrillage 
    en prenant environ des point tous les 0.01° en longitude et 0.005° en latitude puis tout ces points sont mis 
    dans un .json utilisé pour la heat map.

    Cette fonction prend aucun paramètre mais pourra par la suite prendre des paramètres 
    de dates pour avopir une carte suivant des dates choisi sur le site flask.
    """
    
    con=psycopg2.connect(database='postgres',
                          user='postgres',
                          host='localhost',
                          password='postgres',
                          port='5432')
    
#selection des données   
    with con:
        cur=con.cursor() 
        
        cur.execute("""SELECT ST_X(pts_bas_gauche) FROM bdlog WHERE code = '200'""")
        x_bg=cur.fetchall()
        
        cur.execute("""SELECT ST_Y(pts_bas_gauche) FROM bdlog WHERE code = '200'""") 
        y_bg=cur.fetchall()
       
        cur.execute("""SELECT ST_X(pts_haut_droit) FROM bdlog WHERE code = '200'""")
        x_hd=cur.fetchall()
        
        cur.execute("""SELECT ST_Y(pts_haut_droit) FROM bdlog WHERE code = '200'""")  
        y_hd=cur.fetchall()
        
    #    print(x_hg,y_hg,x_bd,y_bd) 
    cur.close()  
    con.close()
    
#on remet les xy ensemble 
    p_bg=[]
    p_hd=[]
    c1,c2=0,0
    
    for i in x_bg:
        p_bg.append((y_bg[c1][0],i[0]))
        c1+=1
    
    for i in x_hd:
        p_hd.append((y_hd[c2][0],i[0]))
        c2+=1
    
    #print(p_hg,p_bd) 
    
#création des autres point pour le quadrillage de la bbox
    p_center=[]
    c3=0
    
    for i in p_bg:
        x,t,g=i[0],i[0],i[1]
        dt,dg=p_hd[c3][0]-i[0],p_hd[c3][1]-i[1]
        rdt,rdg=round(dt,2)*100,round(dg,2)*100
#        print (t,g,rdt,rdg)
    #    print(p_hd[c3][0],p_hd[c3][1])
#la boucle if permet d'empcher une erreur de division par 0 si le dt ou dg  < 0.05
        if rdt == 0:
            rdg,rdt=1,1
        for i in range(int(rdg+1)):
            p_center.append((x,g,0.1))
            for i in range(int(rdg)):
                p_center.append((t+dt/rdg,g,0.1))
                t+=dt/rdg
            g+=dg/rdg
            t=x
        c3+=1
    #print(p_center)
    
#ajout des valeur a un fichier json qui pourra être lu par feaflet    
    data=[]
    c5=0
    for i in p_center:
        lat=i[0]
        lon=i[1]
        inten=i[2]
    
        pts =  [lat,lon,inten]
        data.append(pts)
        c5+=1
    
    #Pensez à modifier l'emplacement du fichier selon où la totalité du projet a été placée.
    with open('/web/app/static/app1.json', 'w') as json_file:
        json.dump(data, json_file)
        
    #print(p_hd,p_bg)    
    
    #print(type(x_hg[0][0]))
    #print(x_hg[0][0])

if __name__ == "__main__":
    
    creation_points()
