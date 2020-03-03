#coding: utf-8

"""Ce programme a été réalisé dans le but de créer un outil d'analyse du serveur yeti.
   Ce fichier permet d'afficher la page web sous flask."""
   
import psycopg2
from flask import Flask, render_template, request
import matplotlib.pyplot as plt

#pour le reste du programme con permettera de dialoguer avec la base de donnée

con=psycopg2.connect(database='postgres',
                      user='postgres',
                      host='localhost',
                      password='postgres',
                      port='5432')


def create_app():
    """Cette fonction permet de créer plusieurs routes qui affichent plusieurs pages webs"""
    app = Flask(__name__)
    
    @app.route('/',methods=['GET', 'POST'])
    def homepage():
        """Cette fonction affiche la première page web.
            Elle récupère les valeurs de date rentrer par l'utilisateur pour ensuite affiché 
            le diagramme des fichiers error.log en fonction de ces dates"""
        
        #sauvgarde des dates sous 2 conditions:
        #    - si flask renvoi des données (méthode=post)
        #    - si la valeur du bouton nommer sauver a la valeur Date
        
        if request.method == 'POST':
            if request.form['sauver'] == 'Date stockée' :                
                debut = request.form['debut']
                fin = request.form['fin']
                
                #extraction des données dans la base de donnée bdlog où leur date sont comprisent 
                #ou égale à celles rentrer part l'utilisateur. 
                
                with con:
                    cur=con.cursor() 
                            
                    cur.execute("""SELECT code FROM bdlog WHERE %s <= date AND date <= %s""",(debut,fin))
                    doc=cur.fetchall()
                
                liste_type_erreur=[]
                dict_cpt = {}
                
                #On parcourt chaque ligne de notre selection afin d'avoir uniquement les erreurs. 
                #Au sein de ces erreurs on récupère dans un dictionnaire les types d'erreurs et combien de 
                #fois elles ont été faites.
                
                for colonne in doc:                    
                    if colonne[0]!='200':
                        type_erreur=colonne[0]
                        liste_type_erreur.append(int(type_erreur))
                        if not type_erreur in dict_cpt:
                            dict_cpt[type_erreur] = 0
                        dict_cpt[type_erreur] += 1
                
                #On trie le dictionnaire en ordre décroissant, par rapport aux valeurs.
                
                dict_cpt = sorted(dict_cpt.items(), key=lambda x: x[1], reverse=True)
                
                #Si le dictionnaire a plus de 5 codes d'erreur, on ajoute les valeurs des autres codes 
                #sous une seule, nommée 'autres'. Ce qui donnera un dictionnaire à 6 clés.
                
                if len(dict_cpt) > 5:
                    dict_cpt5 = dict_cpt[:5] + [('autres', sum([x[1] for x in dict_cpt[5:]]))]
                else:
                    dict_cpt5 = dict_cpt             
                
                valeur_erreur=[]
                nom_erreur=[]
                
                #Réalisation du diagramme camembert avec une sauvegarde à la fin
              
                for i in dict_cpt5:
                    valeur_erreur.append(i[1])
                    nom_erreur.append(i[0])
                
                colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'red', 'gray']
                plt.figure()
                plt.pie(valeur_erreur, labels=nom_erreur, colors=colors, 
                        autopct='%1.1f%%', shadow=True, startangle=90)
                plt.axis('equal')
                plt.savefig('/home/formation/Documents/site/app/static/graph.png')


        return render_template('homepage.html')

    @app.route('/carte/')
    def carte():
        """Cette fonction permet d'afficher la page web de statistiques avec la route /stat/"""
        
        return render_template('carte.html')
    
    @app.route('/stat/')
    def stat():
        """Cette fonction permet d'afficher la page web de carte de chaleur avec la route /carte/"""
        
        return render_template('stat.html')
        
    return app
