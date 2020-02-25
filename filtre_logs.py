import numpy as np
import gpstime as g
import os
import re
"""import matplotlib.pyplot as plt
from datetime import datetime
from io import StringIO
import csv"""

tic = g.gpstime()

"""
Sites qui m'ont servi à comprendre le code:
https://codehangar.io/smiple-log-and-file-processing-in-python/
https://docs.python.org/2.7/howto/regex.html
"""
def filtrer (fichier, name):
    
    # Regex est utilisé our extraire lesl ignes qui nous intéresse, ici identifier=Yeti
    ligne_regex = re.compile(r"GET /wps")
    ligne_regex2 = re.compile(r"identifier=Yeti")
    
    # On ajoutera les lignes sélectionnés dans un nouveau fichier.
    output_filename = os.path.normpath("log/log_filtres/"+name+".log")
    # Réécris le fichier, ce qui permet de débuter avec un fichier vide.
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
