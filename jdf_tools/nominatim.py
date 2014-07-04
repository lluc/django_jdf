#!/usr/bin/python
# -*- coding: utf8 -*-

"""
    Project : jour de fete
    Date :2014/03/27
    
"""

import psycopg2 as pg
import python_soundex_fr.soundex_fr as sfr
import semantique
import poids

class nominatim:
    """
    """
    
    def __init__(self) :
        pass
    
    
    def reset(self, user, host) :
        # Connection
        self.connection( user,host)
        cur = self.conn.cursor()
        
        # Vider la table "phonetique"
        cur.execute("TRUNCATE phonetique")
        self.conn.commit()
        
        # Fermeture
        cur.close()
        self.deconnexion()
        
    
    def generation(self, user, host, osm_id, commune):
        # Connection
        self.connection( user,host)
        
        cur = self.conn.cursor()
        
    
        # Récupérer les éléments contenus spatialement
        #  dans l'entité osm_id
        cur.execute(self.requete( osm_id))
        
        res = self.traitement(cur, commune)
        
        f = open('insertion.txt','w')
        for ligne in res :
            f.write(str(ligne)+"\n")
        f.close()
        
         # Ecriture dans la base de données
        self.insertion( res )
        
        # Fermeture
        cur.close()
        self.deconnexion()
    
    
    def connection(self, user, host):
        
        chaine_connexion = "dbname=nominatim user="+\
            user+" host="+host+" port=5432"
        
        # Se connecter à une base existante
        self.conn = pg.connect( chaine_connexion )
        
        
    def deconnexion(self):
        # Fermeture de la connexion
        self.conn.close()
        
        
    def traitement(self, curseur, commune):
        
        # Initialisations
        mot = sfr.soundex_fr()
        sem = semantique.semantic(False)
        pds = poids.weight()
        resultat = []
        
        # Parcourir les réponses
        for ligne in curseur.fetchall() :
            print ligne
            # Si le premier élément existe ...
            if ligne[0] :
                nom = ligne[0]
                
                # Analyser la sémantique
                composants = sem.analyze(nom)
                print "nom : "+nom
                print "composants : "+str(composants)
                
                nom_phonem = ""
                
                # S'il existe un composant ...
                if composants:
                    # Affectation par défaut du type
                    type_ligne = composants["type"]
                    print type_ligne
                    
                    # Concaténer les éléments du nom
                    print composants["name"]
                    for item in composants["name"] :
                        nom_phonem = nom_phonem + item #.decode('Latin-1')
                    print "phonem : "+nom_phonem
                    
                    # Ajouter le nom de la commune
                    nom_phonem = nom_phonem +" "+commune
                    
                    # Encodage phonétique
                    
                    phonetique = mot.analyse( nom_phonem.encode('utf-8') )
                                        
                    # Poids
                    poids_p = pds.search(ligne[2],ligne[3])
                    
                    # -- Affiner la partie sémantique --
                    # tester le type et la classe de la ligne (table "place")
                    classe_place = ligne[2]
                    type_place = ligne[3]
                    
                    # type Station
                    if type_place=="station":
                        type_ligne = "station"
                    elif type_place=="tram_stop" or type_place=="bus_stop" :
                        type_ligne = "station"
                    elif classe_place=="railway" and type_place=="stop" :
                        type_ligne = "station"
                    
                    # Composer la structure du résultat
                    resultat.append({
                        'nom' : phonetique,
                        'osm_id' : str(ligne[4]),
                        'poids' : str(poids_p),
                        'ville' : commune,
                        'type' : type_ligne
                    })
                    
        # Renvoyer le tableau de résultat
        return resultat
        
        
    def insertion(self, tableau):
        """
         Alimenter la table 'phonetique' de la base *Nominatim*.
         
         On utilise les données du paramètre 'tableau'
        """
        
        # Créer un curseur
        curseur = self.conn.cursor()
        
        # Lire les lignes du tableau
        for ligne in tableau :
            print ligne
            # et créer un nouvel enregistrement dan la table "phonetique"
            curseur.execute(
                "INSERT INTO phonetique(nom,osm_id,poids,ville,semantic) VALUES ( %s, %s, %s, %s, %s)",
                    (
                    ligne["nom"],
                    ligne["osm_id"],
                    ligne["poids"],
                    ligne["ville"],
                    ligne["type"]
                    ) )
        
        self.conn.commit()
        curseur.close()
        
    def requete(self, osmid ):
        request = """
        SELECT 
          place.name->'name', 
          place.osm_type, 
          place.class, 
          place.type, 
          place.osm_id
         FROM 
          public.place
         WHERE
          place.name->'name' LIKE '%' AND
          ST_Contains( (
            SELECT
                place2.geometry
            FROM
                public.place AS place2
            WHERE
                place2.osm_id = {osm_id} ), public.place.geometry )
        """.format(osm_id = osmid)
        return request
        
    
    