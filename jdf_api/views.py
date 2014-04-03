#!/usr/bin/python
# -*- encoding: utf8 -*-

from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import connection

from jdf.models import Place, Phonetique
from jdf_api.serializers import PlaceSerializer, PhonetiqueSerializer
from jdf_tools import semantique
from jdf_tools.soundex_fr import soundex_fr


@api_view(['GET'])
def place_detail(request, pk):
    """
    Get a specific place, with the OSM_ID.
    """
    try:
        place = Place.objects.get(osm_id=pk)
    except Place.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PlaceSerializer(place)
        return Response(serializer.data)
        
        
@api_view(['GET'])
def place_name(request, place_name):
    """
    Search a place, using a name.
    """
    try:
        place = Place.objects.filter(name__contains=place_name)
    except Place.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PlaceSerializer(place)
        return Response(serializer.data)
        


def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]


@api_view(['GET'])
def search_place_name(request, place_name):
    """
        Search a place, using a phonetic search with the name
    """
    res = []
    
    try:
        
        # Detecter les elements de la phrase
        s = semantique.semantique()
        composants = s.analyser(place_name)

        # Si l element est nomme ...
        if composants :
            # ... concatener les éléments du nom
            nom_phonem = ""
            for item in composants["nom"] :
                nom_phonem = nom_phonem + item
                
            # Encodage phonetique
            mot = soundex_fr.soundex_fr()
            phonetique = mot.analyse( nom_phonem.decode('latin-1') )
            
            res = Phonetique.objects.filter( nom__startswith=phonetique ).distinct("nom","poids").order_by('poids','nom')
            print "OK"
    
                
            
    except Place.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PhonetiqueSerializer(res, many=True)
        return Response(serializer.data)
