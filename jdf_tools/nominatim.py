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
        
    
    def generation(self, user, host, osm_id):
        # Connection
        self.connection( user,host)
        
        # Listes des communes à générer
        if str(osm_id)=="all" :
            communes = self.collect_communes_toutes()
        else :
            communes = self.collect_communes( int(osm_id) )
        
        self.ecriture_communes( communes )
        
        
    def ecriture_communes(self, communes) :
        cur = self.conn.cursor()
        
        f = open('insertion.txt','w')
        
        for commune in communes :
            f.write("-----------------------\n"+
                str(commune[0])+";"+commune[1].encode("utf-8")+"\n-------------------\n")
            # Récupérer les éléments contenus dans
            #  la liste des commune
            cur.execute(self.requete( commune[0]))
            
            res = self.traitement(cur, commune[1])
            
            for ligne in res :
                f.write(str(ligne)+"\n")
             # Ecriture dans la base de données
            self.insertion( res )
        
        # Fermeture
        f.close()
        cur.close()
        self.deconnexion()
    
    
    def collect_communes(self, osmid):
        
        request = """
        SELECT
            osm_id,
            name->'name' 
        FROM 
            public.placex 
        WHERE 
            admin_level=8 AND 
            class like 'boundary' AND 
            name->'name' LIKE '%' AND
          ST_Contains( (
            SELECT
                place2.geometry
            FROM
                public.place AS place2
            WHERE
                place2.osm_id = {osm_id} ), public.placex.geometry )
        """.format(osm_id = osmid)
        
        # Créer un curseur
        curseur = self.conn.cursor()
        
        # Récupérer les éléments contenus spatialement
        #  dans l'entité osm_id
        curseur.execute(request)
        
        return curseur.fetchall()
        
        
    def collect_communes_toutes(self):
        
        request = """
        SELECT
            osm_id,
            name->'name' 
        FROM 
            public.placex 
        WHERE 
            admin_level=8 AND 
            class like 'boundary' AND 
            name->'name' LIKE '%'
        """
        
        # Créer un curseur
        curseur = self.conn.cursor()
        
        # Récupérer les éléments de type commune (admin_level=8)
        curseur.execute(request)
        
        return curseur.fetchall()
        
        
        
    
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
            # Si le premier élément existe ...
            if ligne[0] :
                nom = ligne[0]
                
                # Analyser la sémantique
                composants = sem.analyze(nom)
                
                nom_phonem = ""
                
                # S'il existe un composant ...
                if composants:
                    # Affectation par défaut du type
                    type_ligne = composants["type"]
                    
                    # Concaténer les éléments du nom
                    for item in composants["name"] :
                        nom_phonem = nom_phonem + item #.decode('Latin-1')
                    
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
                place2.osm_id = {osm_id} AND
                place2.osm_type LIKE 'R'), public.place.geometry )
        """.format(osm_id = osmid)
        return request
        
