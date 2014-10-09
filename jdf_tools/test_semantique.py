#!/usr/bin/python
# -*- encoding: utf-8 -*-

"""
    @license: MIT, see COPYING for details.
"""
from semantique import semantic

def test_addressToLetters():
    s = semantic()
    assert s.addressToLetters(["6","juin"]) == ['six ','juin']
    assert s.addressToLetters(["11","novembre"]) == ['onze ','novembre']
    
    
def test_frenchLetters() :
    s = semantic()
    assert s.frenchLetters(u"â") == 'a'
    assert s.frenchLetters(u"ê") == 'e'
    assert s.frenchLetters(u"É") == 'e'
    assert s.frenchLetters(u"î") == 'i'
    assert s.frenchLetters(u"Î") == 'i'
    assert s.frenchLetters(u"ù") == 'u'

def test_analyze() :
    s = semantic()
    assert s.analyze("r") == {'town': '', 'cp': '', 'type': 'poi', 'name': ['r']}
    assert s.analyze( "Av. du Gal De Gaulle" ) == {'town': '', 'name': [u'g\xe9n\xe9ral',u'de', u'gaulle'], 'number': ['#', '#'], 'way': u'avenue', 'cp': '', 'type': 'address'}
    assert s.analyze( "57 ter rue de la gare 37000 TOURS" ) == {'cp': '', 'name': ['gare', 'trente sept mille ', 'tours'], 'number': ['57', 'ter'], 'town': '', 'way':'rue', 'type':'address'}
    assert s.analyze( "Station de captage d'eau potable" ) == {'town': '', 'cp': '', 'type': 'poi', 'name': ['station','de', 'captage','d', 'eau', 'potable']}
    assert s.analyze( "les 2 lions") == {'town': '', 'cp': '', 'type': 'poi', 'name': ['deux ', 'lions']}
    assert s.analyze( "gare de tours" ) == {'cp': '', 'town': '', 'station': 'gare', 'type': 'station', 'name': ['tours']}
    assert s.analyze( "Gare Montparnasse, Paris") == {'cp': '', 'town': 'paris', 'station': 'gare', 'type': 'station', 'name': ['montparnasse']}
    assert s.analyze( "l'heure tranquille") == {'town': '', 'cp': '', 'type': 'poi', 'name': ['heure', 'tranquille']}
    assert s.analyze( u"allée des érables") == {'town': '', 'name': [u'\xe9rables'], 'number': ['#', '#'], 'way': u'all\xe9e', 'cp': '', 'type': 'address'}
    
def test_postProcessName() :
    s = semantic()
    assert s.postProcessName([]) == []
