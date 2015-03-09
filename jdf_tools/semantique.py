#!/usr/bin/python
# -*- encoding: utf-8 -*-

import pyparsing as pp
import re
import numbers

class semantic :
    def __init__(self, produce=False):
        # Common grammar
        self.sep = pp.Optional(pp.Word(',',exact=1))
        self.town = pp.Optional( pp.Word( pp.alphas ), default="")
        self.cp =  pp.Optional( pp.Word( pp.nums,exact=5) , default="")
        
        # If this class is used to analyze the data
        if produce==False :
            self.alphas_fr = pp.alphas+'éèëêàâûôÉÈËÊçîù0123456789'.decode('utf-8').encode('latin-1')
        else :
            # ... or to generate the data
            self.alphas_fr = pp.alphas+'éèëêàâûôÉÈËÊçîù0123456789'
    
    def frenchLetters(self,sentence):
        """
        Convert specials french letters to standards letters
        """
        sentence = re.sub(ur'â','a',sentence)
        sentence = re.sub(ur'ê','e',sentence)
        sentence = re.sub(ur'É','e',sentence)
        sentence = re.sub(ur'î','i',sentence)
        sentence = re.sub(ur'Î','i',sentence)
        sentence = re.sub(ur'ù','u',sentence)
        return sentence
    
    def shortWords(self,sentence) :
        """
        Delete "short words"
        """
        list_words = [  "l",
                        "la",
                        "le",
                        "les",
                        "du",
                        "des",
                        "un"]
                        
        for word in list_words :
            sentence = re.sub(r'\b'+word+'\s+',' ',sentence)
        
        return sentence
    
    
    def abbreviation(self, sentence) :
        """
        Replace abbreviation
        """
        
        # Replace symbols
        for w in ['-',';',':','\'','.',','] :
            sentence = sentence.replace(w,' ')
        
        # Lower letters
        sentence = sentence.lower()
        
        # Replace abbreviation
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
                [ "all", u' allée '],
                [ "rt", " route "],
                [ "rte", " route "],
                [ "doc", " docteur "],
                [ "dr"," docteur "],
                [ "st", " saint "],
                [ "ste", " sainte "],
                [ "lt", " lieutenant "],
                [ "cpt", " capitaine "],
                [ "cdt", " commandant "],
                [ "gal", u' général '],
                [ "pdt", u' président '],
                [ "mgr", " monseigneur "],
                [ "me", u' maître ' ]
            ]
        
        for d in dico :
            sentence = re.sub(r'\b'+d[0]+'\s+', d[1],sentence)
        
        return sentence
    
    
    def analyze( self, sentence):
        """
        This module analyze the sentence.
        It returns a dictionnary matching a pattern. (or default)
        """
        
        sentence = self.abbreviation( sentence )
        sentence = self.frenchLetters( sentence )
        sentence = self.shortWords( sentence )


        # Tests
        #-------

        resStation = self.parserStation( sentence )
        if resStation["name"] != "" :
            # It's a station
            
            # Post-processing
            resStation["name"] =self.postProcessName( resStation["name"] )
            
            return resStation
        
        resaddress = self.parserAddress( sentence )
        if resaddress["name"] != "" :
            # It's an  address
            
            # Post-processing
            resaddress["name"] = self.postProcessName( resaddress["name"] )
            
            return resaddress
        
        # Default pattern/type
        resDefault = self.parserDefault(sentence)
        
        # Post-processing
        resDefault["name"] = self.postProcessName( resDefault["name"] )
        
        return resDefault
        
    
    def postProcessName(self, words):
        # Convert the numbers
        words =self.addressToLetters( words )
        
        # Delete all the "d'" and "de" that they 
        #  are not of the name
        list_words = [  "de",
                        "du",
                        "des",
                        "d"]
        if len(words)>=1 :
            if words[0] in list_words :
                del words[0]    

        return words
        
        
    def addressToLetters(self, address) :
        """
        Convert the numbers contained in an address to words
        """
        n = numbers.numbers()
        for i in range(0,len(address)) :
            if address[i].isdigit()==True :
                address[i] = n.convNumber2letter(int(address[i])).lower()
        return address
        
        
    def parserDefault(self,sentence) :
        """
        Default parser.
        Slice the sentence into tokens.
        """
        # Initializing results
        result = {}
        
        # Grammar
        nom = pp.Group( pp.OneOrMore( pp.Word(self.alphas_fr) ) + pp.Suppress(self.sep))
        defaut = pp.Optional(nom, default="")  + self.cp + self.town
        
        # Slice the sentence
        jetons = defaut.parseString( sentence )
        result["name"] = [ i for i in jetons[0] ]
        result["cp"] = jetons[1]
        result["town"] = jetons[2]
        result["type"] = "poi"

        return result
        
    
    def parserAddress(self, sentence) :
        """
        Recognizing components of an address
        """
        ways = [
            "place",
            "square",
            "carrefour",
            "cours",
            "mail",
            u"allée",
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
        
        # Initializing results
        result = {}

        # Grammar of an address
        name = pp.Group( pp.OneOrMore( pp.Word(self.alphas_fr) ) + pp.Suppress(self.sep))
        way = pp.oneOf( ways )
        number =  pp.Group(pp.Word( pp.nums))
        number2 =  pp.Group(pp.Word( pp.nums) + pp.Optional( pp.Word(pp.alphas)) )
        
        # Using the grammar
        address1 =pp.Suppress(self.sep) +\
            way + pp.Optional(name, default="") + self.cp + self.town
        address = pp.Optional( number, default="##" ) + address1
        address2 = pp.Optional( number2, default="##" ) + address1
            
        try:
            # Detect if sentence is matching address pattern
            #  (only numbered adress. Ex = 1 )
            tokens = address.parseString( sentence )
            result["number"] = [ i for i in tokens[0] ]
            result["way"] = tokens[1]
            result["name"] = [ i for i in tokens[2] ]
            result["cp"] = tokens[3]
            result["town"] = tokens[4]
            result["type"] ="address"
        except :
            try:
                # Detect if sentence is matching address2 pattern
                #  (number followed by a letter. Ex = 1B )
                tokens = address2.parseString( sentence )
                result["number"] = [ i for i in tokens[0] ]
                result["way"] = tokens[1]
                result["name"] = [ i for i in tokens[2] ]
                result["cp"] = tokens[3]
                result["town"] = tokens[4]
                result["type"] ="address"
            except :
                # Fill empty fields
                result["number"] = ""
                result["way"] = ""
                result["name"] = ""
                result["cp"] = ""
                result["town"] = ""
                result["type"] = ""
        return result
        
        
    def parserStation(self, sentence) :
        """
        Recognizing items of public transports
        """
        
        # Stop-words for stations
        stations = [
            u'arrêt',
            "arret",
            "gare"
            ]
        
        # Initializing results
        result = {}
        
        # Grammar of station
        station_type = pp.oneOf( stations )
        name = pp.Group( pp.OneOrMore( pp.Word( self.alphas_fr ) ) + pp.Suppress(self.sep))
        
        # Using grammar to slicing
        station = station_type + pp.Optional(name, default="")  + self.cp + self.town
        
        try:
            # Detect if sentence is matching station pattern
            tokens = station.parseString( sentence )
            test_station = True
            result["station"] = tokens[0]
            result["name"] = [ i for i in tokens[1] ]
            result["cp"] = tokens[2]
            result["town"] = tokens[3]
            result["type"] ="station"
        except :
            # Fill empty fields
            result["number"] = ""
            result["way"] = ""
            result["name"] = ""
            result["cp"] = ""
            result["town"] = ""
            result["type"] = ""
            
        return result
    
    
if __name__ == '__main__':
    s = semantic()

    print s.analyze( "r" )
    print s.analyze( "rue" )
    print s.analyze( "rue de" )
    print s.analyze( "rue de la " )
    print s.analyze( "rue de la gare" )
    print s.analyze( "4b, rue de la gare" )
    print s.analyze( "56 ter, rue de la gare" )
    print s.analyze( "56 ter, rue de la gare, TOURS" )
    print s.analyze( "56 ter, rue de la gare,37 TOURS" )
    print s.analyze( "57 ter rue de la gare 37000 TOURS" )
    print s.analyze( "Boulevard d'Italie, Paris" )
    print s.analyze( "rue du Dr. faton" )
    print s.analyze( "Av. du Gal De Gaulle" )
    print s.analyze( "gare de tours" )
    print s.analyze( "Rue Désiré Lecomte tours" )
    print s.analyze( "Rue de la Cave Lagas")
    print s.analyze( "Gare Montparnasse")
    print s.analyze( "Gare Montparnasse, Paris")
    print s.analyze( "clos" )
    print s.analyze( u"allée hector" )
    print s.analyze( "Jules Verne" )
    print s.analyze( "Jules Verne, nantes" )
    print s.analyze( "Station de captage d'eau potable" )
    print s.analyze( "58 rue colbert" )
    print s.analyze( "58b rue colbert" )
    print s.analyze( "arrêt palais")
    print s.analyze( "la grande bruère")
    print s.analyze( "charles lindbergh")
    print s.analyze( "l'heure tranquille")
    print s.analyze( "rue du 11 novembre")
    print s.analyze( "les 2 lions")
    print s.analyze( u"île simon")
    print s.analyze( u"ile simon")
    print s.analyze( u"allée des érables")
    
