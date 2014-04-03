from django.db import models
from django_hstore import hstore

# Create your models here.
class Place(models.Model):
    osm_type = models.CharField(max_length=1)
    osm_id = models.IntegerField(primary_key=True)
    class_field = models.TextField(db_column='class') # Field renamed because it was a Python reserved word.
    type = models.TextField()
    name = hstore.DictionaryField(blank=True) # This field type is a guess.
    admin_level = models.IntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    street = models.TextField(blank=True)
    isin = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    extratags = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField() # This field type is a guess.
    
    objects = hstore.HStoreManager()
    
    class Meta :
        managed = False
        db_table= 'place'

class Phonetique(models.Model):
    id = models.IntegerField(null=False, primary_key=True)
    nom = models.TextField()
    #osm_id = models.IntegerField()
    osm = models.ForeignKey(Place)
    poids = models.IntegerField()
    
    class Meta :
        managed = False
        db_table ='phonetique'
        
    def __unicode__(self):
        return '%d, %s, %s' % (self.poids, self.nom, self.osm)
