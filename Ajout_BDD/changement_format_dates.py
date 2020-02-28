# -*- coding: utf-8 -*-
"""
Ce programme a été réalisé dans le but de créer un outil d'analyse du serveur Yéti, et permet de changer le format de date du fichier access.log.
"""

import os
import re
import datetime as dt
import locale

#https://stackoverflow.com/questions/955986/what-is-the-correct-way-to-set-pythons-locale-on-windows
#Etape importante, car il nous faut lire les nom des mois en anglais, et non en français! Donc ici on change de locale pour lire les strings.

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

def replace_date(file, name):
    """
    Fonction qui prend en entrée un string de l'emplacement du fichier, et un string pour donner un nom au nouveau .log créé, et retourne le string de l'emplacement du nouveau fichier.
    
    Cette fonction remplace le format de date du fichier access.log par celui du fichier erreur.log
    """
    
    output_filename = os.path.normpath("log/changement_date/"+name+".log")
    with open(output_filename, "w") as out_file:
        out_file.write("")
    
    #Ici on lit notre fichier, et dans la nouvelle liste, on lui insère les dates.
    
    lst_date = []

    with open(file, "r") as in_file:
        for line in in_file:
            expression_regex = re.compile(r"([0-9]+\/[a-z]+\/[0-9]+)", re.IGNORECASE)
            result = expression_regex.findall(line)
            lst_date.append(result[0])
                
    l = []
    for e in lst_date:
        val = dt.datetime.strptime(e, "%d/%b/%Y")
        chgt_date = val.strftime("%Y/%m/%d")
        l.append(chgt_date)

    #Le compteur est nécessaire pour passer par tous les élements de la liste.
    
    cpt = 0
    
    with open(output_filename, "a") as out_file:
        with open(file, "r") as in_file:
            for line in in_file:
                expression_regex = re.compile(r"([0-9]+\/[a-z]+\/[0-9]+)", re.IGNORECASE)
                result = expression_regex.findall(line)
                out_file.write(line.replace(result[0], l[cpt]))
                cpt += 1
    print("fichier access avec les nouvelles dates sauvergardé dans:", output_filename)
    return output_filename
