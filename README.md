django_jdf
==========

---

## Digest (in English)

*Django_jdf* is a Django application to help people who wants to performs smart search in the "Nominatim" database. *Django_jdf* is developped to be used by the "Geo-velo"'s website. [Géovélo](http://www.geovelo.fr/).

The goal of *Django_jdf* is to serve a geocoding service based on "Nominatim" upon a small area (e.g : City, Region, District, County, ... )

Currently, the only supported language (in search) is french language.

The name "Jour de Fête" ( aka JDF in this module) comes from a french film of Jacques Tati : in a small village, a postman wants to optimize his circuit.

---

## Résumé

*Django_jdf* est une application Django destinée à améliorer l'expérience utiliseur, en ce qui concerne les recherches effectuées en utilisant le base "Nominatim". Ce projet a été développé initialement pour le site *[Géovélo](http://www.geovelo.fr/) .*

Le projet, volontairement, ne prend en charge que le français et la formalisation française des adresses. Pour des moteurs de recherche d'adresses sur des territoires plus vastes, il vaut mieux regarder vers des solutions telles que *[Photon](https://github.com/komoot/photon/)*. (bien que ce dernier soit en Java et non en Python)

Bien que pouvant couvrir la France entière, *Django_jdf* est plutôt destiné à une structure désirant utiliser un géocodeur, ou une recherche d'adresse avec auto-complétion, sur un territoire donné (ex: Département, communauté de communes, commune, ... )

## Architecture

La base *Nominatim* n'est pas altérée. On lui adjoint seulement une table *phonetique*. Celle-ci sert à stocker une chaine phonétique (calculé par un SoundEx personnalisé) et un "poids" qui permet de hiérarchiser l'affichage des réponses.

Lors d'une recherche, *Django_jdf* renvoie une réponse au format JSON. C'est cette réponse qui pourra être utilisée dans une saisie avec auto-complétion.

## Installation

### Sources

Récupérer les sources sur Github :

       git clone --recursive  https://github.com/lluc/django_jdf.git

### Dépendances

Pour installer les modules Django utilisés dans ce projet, consulter le fichier *requirements.txt". Il est possible d'installer automatiquement ces modules, en utilisant une commande du type :

	 pip install -r requirements.txt

### Paramètres

Il n'y a pas de fichier *settings.py* ( dans le répertoire *django_jdf* ).  A la place, on utilise le fichier *local_settings.py*. On appelle ce fichier en modifiant le source de *manage.py*, avec cette ligne :

      os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_jdf.local_settings") 

Suivant la situation (développement ou production) on fait appel à l'un de ces deux fichiers :  *devel_settings.py* ou *prod_settings.py*. L'appel  se fait au sein de *local_settings.py* au travers de ce type de commande :

- pour les paramètres de développement :

                       from devel_settings import *

- pour les paramètres de production :

                       from prod_settings import *

Le fichier *prod_settings.py* pourrait être de la forme suivante :


	DEBUG = False

	ADMINS = (
	    # ('Your Name', 'your_email@example.com'),
	)

	DATABASES = {
	    'default': {
	        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
	        'NAME': 'nominatim',                      # Or path to database file if using sqlite3.
	        # The following settings are not used with sqlite3:
	        'USER': '******',
	        'PASSWORD': '******',
	        'HOST': '***.***.***.***',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
	        'PORT': '5432',                      # Set to empty string for default.
	    }
	}


## Fonctionnement

### Génération
La génération concerne la production de données, au sein de la base Nominatim, pour pouvoir, ensuite, effectuer des requêtes phonétiques et sémantiques.

Cette génération d'effectue dans une console, sur le serveur.

#### Génération d'une commune
On récupére dans OpenStreetMap le numéro de la relation de la limite administraive de la commune.
Par exemple, pour la ville de Tours, ce sera l'identifiant **76306**. Donc, pour effectuer la génération, on exécute la commande suivante ( en remplaçant les variables *<user>* et *<password>* ) :

	python manage.py generation  <user> <password> 62.210.146.189 76306
	
On peut utiliser ce type de commande pour tout type d'entité administrative qui est identifiée dans OpenStreetMap par une relation (département, région, arrondissement, ... )
	
#### Effacement des données
Pour effacer la totalité des données contenues dans la table *phonetique*, exécuter la commande suivante :

	python manage.py generation  --reset <user> <password> 62.210.146.189
	
#### Génération globale
La génération globale concerne l'ensemble de la France métropolitaine. Elle s'effectue en utilisant l'identifiant *all* :

	python manage.py generation  <user> <password> 62.210.146.189 all

	

### Requêtage
On utilise la biliothèque *Django Rest Framework* ( [site](http://www.django-rest-framework.org/) ). 
Les sources de requêtages se trouvent dans le répertoire qui gère l'API : *jdf_api*

C'est le fichier *views.py* qui contient les requêtes à la base de données.





