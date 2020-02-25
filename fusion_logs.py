import numpy as np
import gpstime as g
import os
import re

def fusion(file1, file2):
    """
    Fonction qui fusionne les données des deux fichiers en un seul. On créé un nouveau fichier
    en premier temps.
    """
    output_filename = os.path.normpath("log/fusion/fusion.log")
    with open(output_filename, "w") as out_file:
        out_file.write("")
        
    with open(output_filename, "a") as out_file:
        """
        On lit les deux fichiers.
        """
        with open(file2, "r") as in_file2:
            with open(file1, "r") as in_file:
                """lst_total sert à contenir les listes regroupant tous les paramètres souhaité de la ligne correspondante."""
                
                lst_total = []
                
                for line in in_file:
                    """On récupère la date et l'heure de access, et on écrit chaque ligne du fichier access dans le nouveau fichier."""
                    
                    date1 = re.compile(r"([0-9]+\/[0-9]+\/[0-9]+)")
                    res1_1 = date1.findall(line)
                        
                    heure1 = re.compile(r"\:([0-9]+\:[0-9]+\:[0-9]+)")
                    res1_2 = heure1.findall(line)
                    
                    expression_regex1 = re.compile(r'([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+) - - \[([0-9]+\/[0-9]+\/[0-9]+)\:([0-9]+\:[0-9]+\:[0-9]+).*methode=(.*);.*bbox=(.*[0-9]+\.[0-9]+),(.*[0-9]+\.[0-9]+),(.*[0-9]+\.[0-9]+),(.*[0-9]+\.[0-9]+);risque_haut=(.*);risque_bas=(.*);seuil_alti=(.*);rdv=([^;]+);potentiel_danger=(.*);neige_mouillee=([^;]+);taille_groupe=(.*) .*\ ([0-9]+) [0-9]+', re.I)
                    result1 = expression_regex1.findall(line)
                   
                    if not (result1):
                        pass
                    else:
                        """Les fichiers ont 16 groupes en tout, donc on va les récupérer un à un, puis les append dans une liste. Les descriptions des erreurs ne seront que ajouté si la condition est remplie."""
                        listeru = []
                    
                        for i in range(16):
                            get_group = expression_regex1.search(line).group(i+1)
                            listeru.append(get_group)
                        
                        val_str = 'None'

                    for lineru in in_file2:
                        """Idem, mais pour le fichier error."""
                        
                        date2 = re.compile(r"([0-9]+\/[0-9]+\/[0-9]+)")
                        res2_1 = date2.findall(lineru)
                        
                        heure2 = re.compile(r"([0-9]+\:[0-9]+\:[0-9]+)")
                        res2_2 = heure2.findall(lineru)
                        expression_regex2 = re.compile(r"\*([0-9]+.*), client")
                        result2 = expression_regex2.findall(lineru)
                        
                        if (res1_1[0] == res2_1[0]) and (res1_2[0] == res2_2[0]):
                            """Si les deux dates et heures sont les mêmes, on prend les paramètres
                            qui nous intéresse, et les ajoute dans une ligne de notre
                            nouveau fichier."""
                            if not (result2):
                                pass
                            else:
                                val_str = str(result2[0])
                    
                    """Saut de ligne car il le faut."""
                    listeru.append(val_str)
                    lst_total.append(listeru)
                    out_file.write(str(listeru) + "\n")
                    in_file2.seek(0)
    print("fichier fusioné sauvergardé dans:",output_filename)
    return output_filename
