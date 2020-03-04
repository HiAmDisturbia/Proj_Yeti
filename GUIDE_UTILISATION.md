# Guide d'utilisation

## Installation des bibliothèques

Suivre ce qui est écrit dans "GUIDE_INSTALL" pour installer en avance les bibliothèques qui seront utilisé pour les programmes, car certaines ne sont pas pré-installées sur Python.

## Exécution des codes

### Avant de les exécuter

Sur pgadmin3, si il n'y a pas de serveurs, il faut en importer/créer un, et que ce soit un localhost.
Pour les connexions à la base de données:
- Nom du serveur: ```postgres```
- Hôte: ```localhost```
- Port TCP: ```5432``` #à vérifier par vous-même, si non rempli
- Nom de l'utilisateur: ```postgres```
- Mot de passe: ```postgres```

### Exécution des scripts Python

Saisir les fichiers access.log et error.log dans le script "ajout_donnees_a_bdd.py" pour filtrer les fichiers logs, et les ajouter à la base de données.
Ensuite, exécuter "création_json_heatmap.py" pour créer la carte de chaleur.
Enfin, lancer "run.sh" pour lancer les scripts flask pour afficher la page web.

## Utilisation de la page web

Saisir les dates souhaitées dans les zones de texte.
Enfin, vous pouvez visualiser les résultats en cliquant sur "Statistiques" et "Carte de chaleur".
```#NB: Seul Statistiques prend en compte les dates.```
