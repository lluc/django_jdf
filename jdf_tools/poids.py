#!/usr/bin/python
# -*- encoding: utf8 -*-

import csv


class poids:
    def __init__(self):
        self.dict_poids = []
        self.charger()
        
    def charger(self):
        """
         Charger les paramètres contenus dans le fichier *poids.csv*
        """
        fichier = open('poids.csv', 'r')
        lecteur = csv.reader(fichier, delimiter=',')
        for ligne in lecteur :
            if len(ligne)==3 :
                self.dict_poids.append({
                    'classe' : ligne[0],
                    'type' : ligne[1],
                    'poids' : ligne[2]
                })
        fichier.close()

    def chercher(self,classe,typ) :
        """
            Renvoyer un poids, en focntion de la classe et du type
            demandés.
        """
        for ligne in self.dict_poids :
            if ligne['classe']==classe and ligne['type']== typ :
                return ligne['poids']
        
        # Valeur par défaut :
        return 100


if __name__ == '__main__':
    p = poids()
    print p.dict_poids
    print p.chercher("highway","secondary")
    print p.chercher("highway","path")
    print p.chercher("highway","track")
    print p.chercher("highway","toto")
    
    
