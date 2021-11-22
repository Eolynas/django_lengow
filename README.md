# Django Lengow


[![version-python](https://img.shields.io/static/v1?label=Python&message=3.7&color=065535)]()
[![made-with-python](https://img.shields.io/badge/Made%20with-Django-1f425f.svg)]()


--------------
# Détail du projet

Le but de ce test est de comprendre votre utilisation de Django. 
Il n'y a pas de piège, nous voulons simplement mesurer votre niveau technique. 
Le but est de récupérer des produits provenant d'un flux xml et de les manipuler. 
Vous pouvez utiliser le SGBD que vous souhaitez.

--------------
# Fonctionnalités
- Création d'une commande Django permettant de récupérer les commandes de l'API et de les enregistrer en base de données.
- Créer les vues nécessaires pour:
  - lister les commandes
  - lister 1 commande 
  - rechercher selon les champs du modèle et afficher les résultats.


--------------
# Installation
Création de la base de données
```
La base de données est deja présente (base de donnée SQLite (db.sqlite3)
```

Création de l'environnement virtuel
```
virtualenv venv
source venv/bin/activate
```

Installation des dépendances

```
pip install -r requirements.txt
```


Faire la migration de la base de données
```
python manage.py migrate
```
Création des variables d'environnement:
```
DJANGO_SETTINGS_MODULE=settings.production 
```

--------------
# Liste des commandes

Insertion des données XML dans la base de données
```
python3 manage.py insert_data_xml
```
--------------
# Author

Développeur: Eddy Hubert

Contact: contact@eddy-hubert.fr
