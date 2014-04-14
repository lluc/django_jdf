#!/usr/bin/python
# -*- encoding: utf8 -*-

import pyparsing as pp
import re

class semantique :
    def __init__(self):
        # Définitions communes de grammaire
        self.sep = pp.Optional(pp.oneOf(","))
        self.ville = pp.Optional( pp.Word( pp.alphas ), default="")
        self.cp =  pp.Optional( pp.Word( pp.nums,exact=5) , default="")
        
        self.alphas_fr = pp.alphas+"éèëêàâûôÉÈËÊç"
    
    def abbreviation(self, phrase) :
        """
        Remplacer les abréviations communes
        """
        phrase = phrase.encode('latin-1')
        
        # Remplacer les symboles
        for w in ['-',';',':','\'','.'] :
            phrase = phrase.replace(w,' ')
        
        # Mettre en minuscules
        phrase = phrase.lower()
        
        # Remplacer les abbréviations
        dico = [ ['/'," sur "],
                [ "bld"," boulevard "],
                [ "bd", " boulevard "],
                [ "av"," avenue "],
                [ "ave"," avenue "],
                [ "fg"," faubourg "],
                [ "fb"," faubourg "],
                [ "fbg", " faubourg "],
                [ "pl", " place "],
                [ "sq", " square "],
                [ "imp", " impasse "],
                [ "ch", " chemin "],
                [ "che", " chemin "],
                [ "all", " allée "],
                [ "rt", " route "],
                [ "rte", " route "],
                [ "doc", " docteur "],
                [ "dr"," docteur "],
                [ "st", " saint "],
                [ "ste", " sainte "],
                [ "lt", " lieutenant "],
                [ "cpt", " capitaine "],
                [ "cdt", " commandant "],
                [ "gal", " général "],
                [ "pdt", " président "],
                [ "mgr", " monseigneur "],
                [ "me", " maître " ]
            ]
        
        for d in dico :
            phrase = re.sub(r'\b'+d[0]+'\s+', d[1],phrase)
        
        return phrase
    
    
    def analyser( self, phrase):
        """
        Ce module analyse les phrases qui lui sont passées.
        En fonction du motif identifié, il renvoie 'None' ou un
        dictionnaire correspondant au motif.
        """
        
        phrase = self.abbreviation( phrase )
        
        # Tests
        #-------
        
        resStation = self.parserStation( phrase )
        if resStation["nom"] != "" :
            # C'est une station
            return resStation
        
        resAdresse = self.parserAdresse( phrase )
        if resAdresse["nom"] != "" :
            # C'est une adresse
            return resAdresse
        
        return self.parserDefaut( phrase )
        
    
    def parserDefaut(self,phrase) :
        """
        Parser par défaut.
        Tronçonner les différents mots.
        """
        # Initialisation des résultats
        result = {}
        
        # Définir la grammaire
        nom = pp.Group( pp.OneOrMore( pp.Word(self.alphas_fr) ) + pp.Suppress(self.sep))
        defaut = pp.Optional(nom, default="")  + self.cp + self.ville
        
        # Découper la phrase
        jetons = defaut.parseString( phrase )
        result["nom"] = jetons[0]
        result["cp"] = jetons[1]
        result["ville"] = jetons[2]
        result["type"] = "poi"

        return result
        
    
    def parserAdresse(self, phrase) :
        """
        Reconnaissance des éléments d'une adresse
        """
        voies = [
            "place",
            "square",
            "carrefour",
            "cours",
            "mail",
            "allée",
            "promenade",
            "chemin",
            "voie",
            "rue",
            "impasse",
            "ruelle",
            "passage",
            "avenue",
            "boulevard"
            ]
        
        # Initialisation des résultats
        result = {}
        
        # Définir la grammaire d'une adresse
        nom = pp.Group( pp.OneOrMore( pp.Word(self.alphas_fr) ) + pp.Suppress(self.sep))
        voie = pp.oneOf( voies )
        numero = pp.Group( pp.Word( pp.nums) + pp.Optional(pp.Word(pp.alphas) ) )
        
        # TODO : prise en charge des accents.
        
        # Utiliser cette grammaire pour décomposer une adresse
        adresse = pp.Optional( numero, default="##" ) + pp.Optional( pp.Suppress(self.sep) ) +\
            voie + pp.Optional(nom, default="")  + self.cp + self.ville
            
        try:
            # Détecter si la phrase correspond à un motif d'adresse
            jetons = adresse.parseString( phrase )
            result["numero"] = jetons[0]
            result["voie"] = jetons[1]
            result["nom"] = jetons[2]
            result["cp"] = jetons[3]
            result["ville"] = jetons[4]
            result["type"] ="adresse"
        except :
            result["numero"] = ""
            result["voie"] = ""
            result["nom"] = ""
            result["cp"] = ""
            result["ville"] = ""
            result["type"] = ""
        return result
        
        
    def parserStation(self, phrase) :
        """
        Reconnaissance des éléments d'un arrêt de transports en commun
        """
        
        # Termes se référant à une notion de station
        stations = [
            "arrêt",
            "gare"
            ]
        
        # Initialisation des résultats
        result = {}
        
        # Définir la grammaire d'une station
        station_type = pp.oneOf( stations )
        nom = pp.Group( pp.OneOrMore( pp.Word( self.alphas_fr ) ) + pp.Suppress(self.sep))
        
        # Utiliser cette grammaire pour décomposer le nom d'une station
        station = station_type + pp.Optional(nom, default="")  + self.cp + self.ville
        
        try:
            # Détecter si la phrase correspond à un motif de station
            jetons = station.parseString( phrase )
            test_station = True
            result["station"] = jetons[0]
            result["nom"] = jetons[1]
            result["cp"] = jetons[2]
            result["ville"] = jetons[3]
            result["type"] ="station"
        except :
            # Remplir des champs vides
            result["station"] = ""
            result["nom"] = ""
            result["cp"] = ""
            result["ville"] = ""
            result["type"] = ""
            
        return result



if __name__ == '__main__':
    s = semantique()

    print s.analyser( "r" )
    print s.analyser( "rue" )
    print s.analyser( "rue de" )
    print s.analyser( "rue de la " )
    print s.analyser( "rue de la gare" )
    print s.analyser( "4b, rue de la gare" )
    print s.analyser( "56 ter, rue de la gare" )
    print s.analyser( "56 ter, rue de la gare, TOURS" )
    print s.analyser( "56 ter, rue de la gare,37 TOURS" )
    print s.analyser( "57 ter rue de la gare 37000 TOURS" )
    print s.analyser( "Boulevard d'Italie, Paris" )
    print s.analyser( "rue du Dr. faton" )
    print s.analyser( "Av. du Gal De Gaulle" )
    print s.analyser( "gare de tours" )
    print s.analyser( "Rue Désiré Lecomte tours" )
    print s.analyser( "Rue de la Cave Lagas")
    print s.analyser( "Gare Montparnasse")
    print s.analyser( "Gare Montparnasse, Paris")
    print s.analyser( "clos" )
    print s.analyser( "allée hector" )
    print s.analyser( "Jules Verne" )
    print s.analyser( "Jules Verne, nantes" )
    
    

