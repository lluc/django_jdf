django_jdf
==========

---

## Digest (in English)

*Django_jdf* is a Django application to help people who wants to performs smart search in the "Nominatim" database. *Django_jdf* is developped to be used by the "Geo-velo"'s website. [Géovélo](http://www.geovelo.fr/).

The goal of *Django_jdf* is to serve a geocoding service based on "Nominatim" upon a small area (e.g : City, Region, District, County, ... )

Currently, the only supported language (in search) is french language.

The name "Jour de Fête" ( aka JDF in this module) comes of a french film of Jacques Tati : in a small village, a postman wants to optimize his circuit.

---

## Résumé

*Django_jdf* est une application Django destinée à améliorer l'expérience utiliseur, en ce qui concerne les recherches effectuées en utilisant le base "Nominatim". Ce projet a été développé initialement pour le site *[Géovélo](http://www.geovelo.fr/) .*

Le projet, volontairement, ne prend en charge que le français et la formalisation française des adresses. Pour des moteurs de recherche d'adresses sur des territoires plus vastes, il vaut mieux regarder vers des solutions telles que *[Photon](https://github.com/komoot/photon/)*. (bien que ce dernier soit en Java et non en Python)

Bien que pouvant couvrir la France entière, *Django_jdf* est plutôt destiné à une structure désirant utiliser un géocodeur, ou une recherche d'adresse avec auto-complétion, sur un territoire donné (ex: Département, communauté de communes, commune, ... )

## Architecture

La base *Nominatim* n'est pas altérée. On lui adjoint seulement une table *phonetique*. Celle-ci sert à stocker une chaine phonétique (calculé par un SoundEx personnalisé) et un "poids" qui permet de hiérarchiser l'affichage des réponses.

Lors d'une recherche, *Django_jdf* renvoie une réponse au format JSON. C'est cette réponse qui pourra être utilisée dans une saisie avec auto-complétion.




