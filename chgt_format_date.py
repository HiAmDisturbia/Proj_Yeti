import numpy as np
import gpstime as g
import os
import re
import datetime as dt
import locale
"""
https://stackoverflow.com/questions/955986/what-is-the-correct-way-to-set-pythons-locale-on-windows
Etape importante, car il nous faut lire les nom des mois en anglais, et non en français
Donc ici on change de locale pour lire les strings.
"""
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
def replace_date(file, name):
    output_filename = os.path.normpath("log/changement_date/"+name+".log")
    with open(output_filename, "w") as out_file:
        out_file.write("")
    
    """
    Ici on lit notre fichier, et dans la nouvelle liste, on lui insère les dates.
    """
    lst_date = []

    with open(file, "r") as in_file:
        for line in in_file:
            expression_regex = re.compile(r"([0-9]+\/[a-z]+\/[0-9]+)", re.IGNORECASE)
            result = expression_regex.findall(line)
            lst_date.append(result[0])
                

    """
    Remerciements à locale pour la lecture des formats de dates. C'est ici que l'on modifie
    le format de date, en premièrement récupérant le sien, puis on le transforme en celui 
    recherché, qui correspond à celui de Error.
    """
    l = []
    for e in lst_date:
        val = dt.datetime.strptime(e, "%d/%b/%Y")
        chgt_date = val.strftime("%Y/%m/%d")
        l.append(chgt_date)
    
    """
    IMPORTANT: Le fichier et la liste des dates contiennent le même nombre d'élements, ce qui nous
    aidera pour créer la boucle dans la fonction replace_date.
    """

    """
    Le compteur est nécessaire pour passer par tous les élements de la liste. On va re-créé un
    fichier log, afin d'avoir les logs d'accès avec le nouveau format de date.
    Pas besoin de retourner quoi que ce soit, étant donné que l'on les mets dans un fichier.
    """
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
