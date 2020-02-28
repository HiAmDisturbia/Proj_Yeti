# -*- coding: utf-8 -*-
"""
Ce programme a été réalisé dans le but de créer un outil d'analyse du serveur Yéti, et permet de fusionner les fichiers access.log et error.log
"""

import os
import re

def fusion(file1, file2):
    """
    Fonction qui prend en entrée deux fichiers, et renvoie un String qui indique l'emplacement du fichier créé dans l'explorateur de fichiers.
    
    Cette fonction rassemble les paramètres des deux fichiers en un seul, en fonction des dates et heures.
    """
    output_filename = os.path.normpath("log/fusion/fusion.log")
    with open(output_filename, "w") as out_file:
        out_file.write("")
        
    with open(output_filename, "a") as out_file:
        with open(file2, "r") as in_file2:
            with open(file1, "r") as in_file:                
                lst_total = [] #Sert à contenir les listes regroupant tous les paramètres souhaité de la ligne correspondante.
                
                for line in in_file:
                    #On récupère la date et l'heure de access, et on écrit chaque ligne du fichier access dans le nouveau fichier.
                    
                    re_date1 = re.compile(r"([0-9]+\/[0-9]+\/[0-9]+)")
                    date1 = re_date1.findall(line)
                        
                    re_heure1 = re.compile(r"\:([0-9]+\:[0-9]+\:[0-9]+)")
                    heure1 = re_heure1.findall(line)
                    
                    expression_regex1 = re.compile(r'([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+) - - \[([0-9]+\/[0-9]+\/[0-9]+)\:([0-9]+\:[0-9]+\:[0-9]+).*methode=(.*);.*bbox=(.*[0-9]+\.[0-9]+),(.*[0-9]+\.[0-9]+),(.*[0-9]+\.[0-9]+),(.*[0-9]+\.[0-9]+);risque_haut=(.*);risque_bas=(.*);seuil_alti=(.*);rdv=([^;]+);potentiel_danger=(.*);neige_mouillee=([^;]+);taille_groupe=(.*) .*\ ([0-9]+) [0-9]+', re.I)
                    result1 = expression_regex1.findall(line)
                    
                    if not (result1):
                        pass
                    else:
                        listeru = [] #Cette liste prend les différents groupes de l'expression regex, et les rassemble.
                    
                        for i in range(16):
                            get_group = expression_regex1.search(line).group(i+1)
                            listeru.append(get_group)
                        
                        val_str = 'None' #Sera utilisé pour prendre le groupe du deuxième fichier.

                    for lineru in in_file2:
                        #On récupère la date et l'heure de error, et on écrit chaque ligne du fichier error dans le nouveau fichier.
                        
                        re_date2 = re.compile(r"([0-9]+\/[0-9]+\/[0-9]+)")
                        date2 = re_date2.findall(lineru)
                        
                        re_heure2 = re.compile(r"([0-9]+\:[0-9]+\:[0-9]+)")
                        heure2 = re_heure2.findall(lineru)
                        expression_regex2 = re.compile(r"\*([0-9]+.*), client")
                        result2 = expression_regex2.findall(lineru)
                        
                        if (date1[0] == date2[0]) and (heure1[0] == heure2[0]):
                            #Comparaisons entre dates et heures, pour ajouter à val_str la valeur du groupe.
                            if not (result2):
                                pass
                            else:
                                val_str = str(result2[0])
                    
                    listeru.append(val_str)
                    lst_total.append(listeru)
                    out_file.write(str(listeru) + "\n")
                    in_file2.seek(0)
    print("fichier fusioné sauvergardé dans:",output_filename)
    return output_filename
