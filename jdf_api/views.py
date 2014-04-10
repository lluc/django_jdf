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
from jdf_tools.python_soundex_fr import soundex_fr


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
    """
    Returns all rows from a cursor as a dict
    """
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
    cursor = connection.cursor()

    try:
        
        # Analyser les elements de la phrase
        #  et les charger dans la structure composants.
        s = semantique.semantique()
        composants = s.analyser(place_name)

        # Si la structure existe ...
        if composants :
            # ... concatener les éléments du nom
            nom_phonem = ""
            for item in composants["nom"] :
                nom_phonem = nom_phonem + item
                
            # Encodage phonetique
            mot = soundex_fr.soundex_fr()
            phonetique = mot.analyse( nom_phonem.decode('latin-1') )
            
            # Ne garder que les noms phonétiques qui correspondent
            # au type voulu (champ 'semantic')
            requete = """
            SELECT
                DISTINCT ph.nom, 
                ph.poids, 
                pl.class, 
                pl.type, 
                ph.ville, 
                ph.semantic, 
                pl.name->'name' AS libelle 
            FROM 
                phonetique AS ph,
                place AS pl 
            WHERE 
                ph.nom LIKE %s AND 
                pl.osm_id = ph.osm_id AND
                ph.semantic LIKE %s
            ORDER BY 
                ph.nom, 
                ph.poids
            """

            cursor.execute( requete,[ phonetique+"%", composants["type"] ] )
            
            
            
    except Place.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(dictfetchall(cursor))
