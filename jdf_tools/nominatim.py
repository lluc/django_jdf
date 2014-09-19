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
    
    
    def reset(self, user, password, host) :
        # Connection
        self.connection( user,password,host)
        cur = self.conn.cursor()
        
        # Vider la table "phonetique"
        cur.execute("TRUNCATE phonetique")
        self.conn.commit()
        
        # Fermeture
        cur.close()
        self.deconnexion()
        
    
    def generation(self, user, password, host, osm_id):
        # Connection
        self.connection( user, password, host)
        
        # Listes des communes à générer
        if str(osm_id)=="all" :
            communes = self.collect_communes_toutes()
        else :
            communes = self.collect_communes( int(osm_id) )
        
        self.ecriture_communes( communes )
        
        
    def ecriture_communes(self, communes) :
        cur = self.conn.cursor()
        
        f = open('insertion.txt','w')
                
        ecriture = [ self.ecriture_commune(cur,commune) for commune in communes ]
        # Fermeture
        f.close()
        cur.close()
        self.deconnexion()
    
    
    def ecriture_commune(self, cur, commune) :
        #f.write("-----------------------\n"+
        #        str(commune[0])+";"+commune[1].encode("utf-8")+"\n-------------------\n")
        
        # Récupérer les éléments contenus dans
        #  la liste des commune
        cur.execute(self.requete( commune[0]))
        
        res = self.traitement(cur, commune[1])
        
        #for ligne in res :
        #   f.write(str(ligne)+"\n")
        
        # Tester si la commune contient des éléments nommés.
        if len(res[0])>=1 :
            # Ecriture dans la base de données
            self.insertion( res )
    
    
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
        
        
        
    
    def connection(self, user, password, host):
        
        chaine_connexion = "dbname=nominatim user="+\
            user+" password="+password+" host="+host+" port=5432"
        
        # Se connecter à une base existante
        self.conn = pg.connect( chaine_connexion )
        
        
    def deconnexion(self):
        # Fermeture de la connexion
        self.conn.close()
        
        
    def traitement(self, curseur, commune):
        
        # Initialisations
        resultat = []
        
        res = [ self.traitement_ligne( ligne, commune ) for ligne in curseur.fetchall() ]
        resultat.append(res)
        
        # Renvoyer le tableau de résultat
        return resultat
        
    def traitement_ligne(self, ligne, commune):
        
        # Initialisations
        mot = sfr.soundex_fr()
        sem = semantique.semantic(False)
        pds = poids.weight()
        resultat=[]
        
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
                    # Encodage phonétique
                    phonetique = mot.analyse( item.encode('utf-8') )
                    nom_phonem = nom_phonem + phonetique 
                
                # Ajouter le nom de la commune
                nom_phonem = nom_phonem + mot.analyse(commune.encode('utf-8'))
                                    
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
                resultat = [nom_phonem, str(ligne[4]),
                    str(poids_p), commune, type_ligne]
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
        args_str = ','.join(curseur.mogrify("(%s,%s,%s,%s,%s)", ligne) for ligne in tableau[0])

        # Exécuter les insertions multiples en rafale
        curseur.execute("INSERT INTO phonetique (nom,osm_id,poids,ville,semantic) VALUES "+args_str)
        
        curseur.close()
        self.conn.commit()
        
        
        
    def requete(self, osmid ):
        request = """
        SELECT 
          place.name->'name', 
          place.osm_type, 
          place.class, 
          place.type, 
          place.osm_id
         FROM 
          public.place, public.place AS place2 
         WHERE
          place.name->'name' NOT LIKE '' AND
          place2.osm_id = {osm_id} AND place2.osm_type LIKE 'R'
          AND ST_Contains(place2.geometry, public.place.geometry)
        """.format(osm_id = osmid)
        return request
        
