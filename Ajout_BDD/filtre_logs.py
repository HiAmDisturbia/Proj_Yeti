# -*- coding: utf-8 -*-
"""
Ce programme a été réalisé dans le but de créer un outil d'analyse du serveur Yéti, et permet de sélectionner les lignes qui nous intéresse.
"""

import os
import re

def filtrer (fichier, name):
    """
    Fonction qui prend en entrée un string de l'emplacement du fichier, et un string pour donner un nom au nouveau .log créé, et retourne le string de l'emplacement du nouveau fichier.
    
    Cette fonction permet de choisir, grâce au regex, les lignes qui nous intéresse.
    """
    ligne_regex = re.compile(r"GET /wps")
    ligne_regex2 = re.compile(r"identifier=Yeti")
    
    # On ajoutera les lignes sélectionnés dans un nouveau fichier.
    output_filename = os.path.normpath("log/log_filtres/"+name+".log")
    
    with open(output_filename, "w") as out_file:
        out_file.write("")
    
    # On incorporera les données dans notre fichier vide, avec le append.
    with open(output_filename, "a") as out_file:
        # On lit le fichier log où l'on veut filtrer les données
        with fichier as in_file:
            # Lis toutes les lignes du fichier
            for line in in_file:
                # Condition pour le filtrage, plus affichage de la ligne, et ajout dans le nouveau fichier
                if (ligne_regex.search(line)) and (ligne_regex2.search(line)):
                    out_file.write(line)
    print("fichier filtré sauvergardé dans:",output_filename)
    return output_filename
