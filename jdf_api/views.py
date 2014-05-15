#!/usr/bin/python
# -*- encoding: utf8 -*-

from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import connection
import logging

from jdf.models import Place, Phonetique
from jdf_api.serializers import PlaceSerializer, PhonetiqueSerializer
from jdf_tools import semantique
from jdf_tools.python_soundex_fr import soundex_fr


FORMAT = '%(asctime)-15s %(module)s %(message)s'
logging.basicConfig(format=FORMAT)
# Get an instance of a logger
logger = logging.getLogger("recherches")


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
    
    logger.info("-----------------------------------")
    logger.info("place : "+place_name)

    try:
        
        # Analyzing items of a sentence
        #  and load them in the components
        s = semantique.semantic()
        components = s.analyze(place_name)

        # IF components exists ...
        if components :
            # ... concatenates items of the name
            name_phonem = ""
            for item in components["name"] :
                name_phonem = name_phonem + item
            logger.info("phonem : "+name_phonem)
            
            # Encode phonetic
            mot = soundex_fr.soundex_fr()
            phonetic = mot.analyse( name_phonem.encode('utf-8'))
            logger.info("phonetic : " + phonetic)
            
            # Filtering on field 'semantic'
            request_sql = """
            SELECT
                ph.nom, 
                ph.poids, 
                pl.class, 
                pl.type, 
                ph.ville, 
                ph.semantic, 
                pl.name->'name' AS libelle,
                ST_Box2D(pl.geometry)
            FROM 
                phonetique AS ph,
                place AS pl 
            WHERE 
                ph.nom LIKE '%s' AND 
                pl.osm_id = ph.osm_id AND
                ph.semantic LIKE '%s'
            ORDER BY 
                ph.nom, 
                ph.poids
            LIMIT 50
            """
            # Fomatting the request
            request_sql = request_sql.replace("\n","")
            request_sql = ' '.join(request_sql.split())
            # Replace known values
            request_sql = request_sql % (phonetic+"%", components["type"])
            
            logger.info("request : " + request_sql )
            
            # Execute request
            cursor.execute( request_sql )
            
            
            
    except Place.DoesNotExist:
        logger.info("404")
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        data = dictfetchall(cursor)
        logger.info("response : ")
        logger.info(data)
        return Response(data)
