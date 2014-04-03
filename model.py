# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80, unique=True)
    class Meta:
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')
    class Meta:
        db_table = 'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)
    class Meta:
        db_table = 'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.BooleanField()
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    class Meta:
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        db_table = 'auth_user_user_permissions'

class Country(models.Model):
    country_code = models.CharField(max_length=2, blank=True)
    country_name = models.TextField(blank=True) # This field type is a guess.
    country_default_language_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'country'

class CountryName(models.Model):
    country_code = models.CharField(max_length=2, blank=True)
    name = models.TextField(blank=True) # This field type is a guess.
    country_default_language_code = models.CharField(max_length=2, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'country_name'

class CountryNaturalearthdata(models.Model):
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'country_naturalearthdata'

class CountryOsmGrid(models.Model):
    country_code = models.CharField(max_length=2, blank=True)
    area = models.FloatField(null=True, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'country_osm_grid'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey('DjangoContentType', null=True, blank=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    class Meta:
        db_table = 'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    class Meta:
        db_table = 'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(max_length=40, primary_key=True)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        db_table = 'django_session'

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    class Meta:
        db_table = 'django_site'

class GbPostcode(models.Model):
    id = models.IntegerField(null=True, blank=True)
    postcode = models.CharField(max_length=9, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'gb_postcode'

class GeographyColumns(models.Model):
    f_table_catalog = models.TextField(blank=True) # This field type is a guess.
    f_table_schema = models.TextField(blank=True) # This field type is a guess.
    f_table_name = models.TextField(blank=True) # This field type is a guess.
    f_geography_column = models.TextField(blank=True) # This field type is a guess.
    coord_dimension = models.IntegerField(null=True, blank=True)
    srid = models.IntegerField(null=True, blank=True)
    type = models.TextField(blank=True)
    class Meta:
        db_table = 'geography_columns'

class GeometryColumns(models.Model):
    f_table_catalog = models.CharField(max_length=256)
    f_table_schema = models.CharField(max_length=256)
    f_table_name = models.CharField(max_length=256)
    f_geometry_column = models.CharField(max_length=256)
    coord_dimension = models.IntegerField()
    srid = models.IntegerField()
    type = models.CharField(max_length=30)
    class Meta:
        db_table = 'geometry_columns'

class ImportNpiLog(models.Model):
    npiid = models.IntegerField(null=True, blank=True)
    batchend = models.DateTimeField(null=True, blank=True)
    batchsize = models.IntegerField(null=True, blank=True)
    starttime = models.DateTimeField(null=True, blank=True)
    endtime = models.DateTimeField(null=True, blank=True)
    event = models.TextField(blank=True)
    class Meta:
        db_table = 'import_npi_log'

class ImportOsmosisLog(models.Model):
    batchend = models.DateTimeField(null=True, blank=True)
    batchsize = models.IntegerField(null=True, blank=True)
    starttime = models.DateTimeField(null=True, blank=True)
    endtime = models.DateTimeField(null=True, blank=True)
    event = models.TextField(blank=True)
    class Meta:
        db_table = 'import_osmosis_log'

class ImportPolygonDelete(models.Model):
    osm_type = models.CharField(max_length=1, blank=True)
    osm_id = models.IntegerField(null=True, blank=True)
    class_field = models.TextField(db_column='class') # Field renamed because it was a Python reserved word.
    type = models.TextField()
    class Meta:
        db_table = 'import_polygon_delete'

class ImportPolygonError(models.Model):
    osm_type = models.CharField(max_length=1, blank=True)
    osm_id = models.IntegerField(null=True, blank=True)
    class_field = models.TextField(db_column='class') # Field renamed because it was a Python reserved word.
    type = models.TextField()
    name = models.TextField(blank=True) # This field type is a guess.
    country_code = models.CharField(max_length=2, blank=True)
    updated = models.DateTimeField(null=True, blank=True)
    errormessage = models.TextField(blank=True)
    prevgeometry = models.TextField(blank=True) # This field type is a guess.
    newgeometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'import_polygon_error'

class ImportStatus(models.Model):
    lastimportdate = models.DateTimeField()
    class Meta:
        db_table = 'import_status'

class LocationArea(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area'

class LocationAreaCountry(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_country'

class LocationAreaLarge(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large'

class LocationAreaLarge0(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_0'

class LocationAreaLarge1(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_1'

class LocationAreaLarge10(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_10'

class LocationAreaLarge100(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_100'

class LocationAreaLarge101(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_101'

class LocationAreaLarge102(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_102'

class LocationAreaLarge103(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_103'

class LocationAreaLarge104(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_104'

class LocationAreaLarge105(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_105'

class LocationAreaLarge106(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_106'

class LocationAreaLarge107(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_107'

class LocationAreaLarge108(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_108'

class LocationAreaLarge109(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_109'

class LocationAreaLarge11(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_11'

class LocationAreaLarge110(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_110'

class LocationAreaLarge111(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_111'

class LocationAreaLarge112(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_112'

class LocationAreaLarge113(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_113'

class LocationAreaLarge114(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_114'

class LocationAreaLarge115(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_115'

class LocationAreaLarge116(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_116'

class LocationAreaLarge117(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_117'

class LocationAreaLarge118(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_118'

class LocationAreaLarge119(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_119'

class LocationAreaLarge12(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_12'

class LocationAreaLarge120(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_120'

class LocationAreaLarge121(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_121'

class LocationAreaLarge122(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_122'

class LocationAreaLarge123(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_123'

class LocationAreaLarge124(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_124'

class LocationAreaLarge125(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_125'

class LocationAreaLarge126(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_126'

class LocationAreaLarge127(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_127'

class LocationAreaLarge128(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_128'

class LocationAreaLarge129(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_129'

class LocationAreaLarge13(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_13'

class LocationAreaLarge130(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_130'

class LocationAreaLarge131(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_131'

class LocationAreaLarge132(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_132'

class LocationAreaLarge133(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_133'

class LocationAreaLarge134(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_134'

class LocationAreaLarge135(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_135'

class LocationAreaLarge136(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_136'

class LocationAreaLarge137(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_137'

class LocationAreaLarge138(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_138'

class LocationAreaLarge139(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_139'

class LocationAreaLarge14(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_14'

class LocationAreaLarge140(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_140'

class LocationAreaLarge141(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_141'

class LocationAreaLarge142(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_142'

class LocationAreaLarge143(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_143'

class LocationAreaLarge144(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_144'

class LocationAreaLarge145(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_145'

class LocationAreaLarge146(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_146'

class LocationAreaLarge147(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_147'

class LocationAreaLarge148(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_148'

class LocationAreaLarge149(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_149'

class LocationAreaLarge15(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_15'

class LocationAreaLarge150(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_150'

class LocationAreaLarge151(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_151'

class LocationAreaLarge152(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_152'

class LocationAreaLarge153(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_153'

class LocationAreaLarge154(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_154'

class LocationAreaLarge155(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_155'

class LocationAreaLarge156(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_156'

class LocationAreaLarge157(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_157'

class LocationAreaLarge158(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_158'

class LocationAreaLarge159(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_159'

class LocationAreaLarge16(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_16'

class LocationAreaLarge160(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_160'

class LocationAreaLarge161(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_161'

class LocationAreaLarge162(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_162'

class LocationAreaLarge163(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_163'

class LocationAreaLarge164(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_164'

class LocationAreaLarge165(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_165'

class LocationAreaLarge166(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_166'

class LocationAreaLarge167(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_167'

class LocationAreaLarge168(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_168'

class LocationAreaLarge169(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_169'

class LocationAreaLarge17(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_17'

class LocationAreaLarge170(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_170'

class LocationAreaLarge171(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_171'

class LocationAreaLarge172(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_172'

class LocationAreaLarge173(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_173'

class LocationAreaLarge174(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_174'

class LocationAreaLarge175(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_175'

class LocationAreaLarge176(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_176'

class LocationAreaLarge177(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_177'

class LocationAreaLarge178(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_178'

class LocationAreaLarge179(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_179'

class LocationAreaLarge18(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_18'

class LocationAreaLarge180(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_180'

class LocationAreaLarge181(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_181'

class LocationAreaLarge182(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_182'

class LocationAreaLarge183(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_183'

class LocationAreaLarge184(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_184'

class LocationAreaLarge185(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_185'

class LocationAreaLarge186(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_186'

class LocationAreaLarge187(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_187'

class LocationAreaLarge188(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_188'

class LocationAreaLarge189(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_189'

class LocationAreaLarge19(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_19'

class LocationAreaLarge190(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_190'

class LocationAreaLarge191(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_191'

class LocationAreaLarge192(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_192'

class LocationAreaLarge193(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_193'

class LocationAreaLarge194(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_194'

class LocationAreaLarge195(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_195'

class LocationAreaLarge196(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_196'

class LocationAreaLarge197(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_197'

class LocationAreaLarge198(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_198'

class LocationAreaLarge199(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_199'

class LocationAreaLarge2(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_2'

class LocationAreaLarge20(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_20'

class LocationAreaLarge200(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_200'

class LocationAreaLarge201(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_201'

class LocationAreaLarge202(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_202'

class LocationAreaLarge203(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_203'

class LocationAreaLarge204(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_204'

class LocationAreaLarge205(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_205'

class LocationAreaLarge206(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_206'

class LocationAreaLarge207(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_207'

class LocationAreaLarge208(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_208'

class LocationAreaLarge209(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_209'

class LocationAreaLarge21(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_21'

class LocationAreaLarge210(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_210'

class LocationAreaLarge211(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_211'

class LocationAreaLarge212(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_212'

class LocationAreaLarge213(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_213'

class LocationAreaLarge214(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_214'

class LocationAreaLarge215(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_215'

class LocationAreaLarge216(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_216'

class LocationAreaLarge217(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_217'

class LocationAreaLarge218(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_218'

class LocationAreaLarge219(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_219'

class LocationAreaLarge22(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_22'

class LocationAreaLarge220(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_220'

class LocationAreaLarge221(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_221'

class LocationAreaLarge222(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_222'

class LocationAreaLarge223(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_223'

class LocationAreaLarge224(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_224'

class LocationAreaLarge225(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_225'

class LocationAreaLarge226(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_226'

class LocationAreaLarge227(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_227'

class LocationAreaLarge228(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_228'

class LocationAreaLarge229(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_229'

class LocationAreaLarge23(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_23'

class LocationAreaLarge230(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_230'

class LocationAreaLarge231(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_231'

class LocationAreaLarge232(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_232'

class LocationAreaLarge233(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_233'

class LocationAreaLarge234(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_234'

class LocationAreaLarge235(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_235'

class LocationAreaLarge236(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_236'

class LocationAreaLarge237(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_237'

class LocationAreaLarge238(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_238'

class LocationAreaLarge239(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_239'

class LocationAreaLarge24(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_24'

class LocationAreaLarge240(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_240'

class LocationAreaLarge241(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_241'

class LocationAreaLarge242(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_242'

class LocationAreaLarge243(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_243'

class LocationAreaLarge244(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_244'

class LocationAreaLarge245(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_245'

class LocationAreaLarge246(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_246'

class LocationAreaLarge247(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_247'

class LocationAreaLarge248(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_248'

class LocationAreaLarge249(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_249'

class LocationAreaLarge25(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_25'

class LocationAreaLarge250(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_250'

class LocationAreaLarge26(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_26'

class LocationAreaLarge27(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_27'

class LocationAreaLarge28(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_28'

class LocationAreaLarge29(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_29'

class LocationAreaLarge3(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_3'

class LocationAreaLarge30(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_30'

class LocationAreaLarge31(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_31'

class LocationAreaLarge32(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_32'

class LocationAreaLarge33(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_33'

class LocationAreaLarge34(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_34'

class LocationAreaLarge35(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_35'

class LocationAreaLarge36(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_36'

class LocationAreaLarge37(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_37'

class LocationAreaLarge38(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_38'

class LocationAreaLarge39(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_39'

class LocationAreaLarge4(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_4'

class LocationAreaLarge40(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_40'

class LocationAreaLarge41(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_41'

class LocationAreaLarge42(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_42'

class LocationAreaLarge43(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_43'

class LocationAreaLarge44(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_44'

class LocationAreaLarge45(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_45'

class LocationAreaLarge46(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_46'

class LocationAreaLarge47(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_47'

class LocationAreaLarge48(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_48'

class LocationAreaLarge49(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_49'

class LocationAreaLarge5(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_5'

class LocationAreaLarge50(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_50'

class LocationAreaLarge51(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_51'

class LocationAreaLarge52(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_52'

class LocationAreaLarge53(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_53'

class LocationAreaLarge54(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_54'

class LocationAreaLarge55(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_55'

class LocationAreaLarge56(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_56'

class LocationAreaLarge57(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_57'

class LocationAreaLarge58(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_58'

class LocationAreaLarge59(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_59'

class LocationAreaLarge6(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_6'

class LocationAreaLarge60(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_60'

class LocationAreaLarge61(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_61'

class LocationAreaLarge62(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_62'

class LocationAreaLarge63(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_63'

class LocationAreaLarge64(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_64'

class LocationAreaLarge65(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_65'

class LocationAreaLarge66(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_66'

class LocationAreaLarge67(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_67'

class LocationAreaLarge68(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_68'

class LocationAreaLarge69(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_69'

class LocationAreaLarge7(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_7'

class LocationAreaLarge70(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_70'

class LocationAreaLarge71(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_71'

class LocationAreaLarge72(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_72'

class LocationAreaLarge73(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_73'

class LocationAreaLarge74(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_74'

class LocationAreaLarge75(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_75'

class LocationAreaLarge76(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_76'

class LocationAreaLarge77(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_77'

class LocationAreaLarge78(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_78'

class LocationAreaLarge79(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_79'

class LocationAreaLarge8(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_8'

class LocationAreaLarge80(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_80'

class LocationAreaLarge81(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_81'

class LocationAreaLarge82(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_82'

class LocationAreaLarge83(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_83'

class LocationAreaLarge84(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_84'

class LocationAreaLarge85(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_85'

class LocationAreaLarge86(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_86'

class LocationAreaLarge87(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_87'

class LocationAreaLarge88(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_88'

class LocationAreaLarge89(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_89'

class LocationAreaLarge9(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_9'

class LocationAreaLarge90(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_90'

class LocationAreaLarge91(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_91'

class LocationAreaLarge92(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_92'

class LocationAreaLarge93(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_93'

class LocationAreaLarge94(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_94'

class LocationAreaLarge95(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_95'

class LocationAreaLarge96(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_96'

class LocationAreaLarge97(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_97'

class LocationAreaLarge98(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_98'

class LocationAreaLarge99(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_large_99'

class LocationAreaRoadfar(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_roadfar'

class LocationAreaRoadnear(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    keywords = models.TextField(blank=True) # This field type is a guess.
    rank_search = models.IntegerField()
    rank_address = models.IntegerField()
    isguess = models.BooleanField(null=True, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_area_roadnear'

class LocationProperty(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property'

class LocationProperty0(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_0'

class LocationProperty1(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_1'

class LocationProperty10(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_10'

class LocationProperty100(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_100'

class LocationProperty101(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_101'

class LocationProperty102(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_102'

class LocationProperty103(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_103'

class LocationProperty104(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_104'

class LocationProperty105(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_105'

class LocationProperty106(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_106'

class LocationProperty107(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_107'

class LocationProperty108(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_108'

class LocationProperty109(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_109'

class LocationProperty11(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_11'

class LocationProperty110(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_110'

class LocationProperty111(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_111'

class LocationProperty112(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_112'

class LocationProperty113(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_113'

class LocationProperty114(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_114'

class LocationProperty115(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_115'

class LocationProperty116(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_116'

class LocationProperty117(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_117'

class LocationProperty118(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_118'

class LocationProperty119(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_119'

class LocationProperty12(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_12'

class LocationProperty120(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_120'

class LocationProperty121(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_121'

class LocationProperty122(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_122'

class LocationProperty123(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_123'

class LocationProperty124(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_124'

class LocationProperty125(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_125'

class LocationProperty126(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_126'

class LocationProperty127(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_127'

class LocationProperty128(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_128'

class LocationProperty129(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_129'

class LocationProperty13(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_13'

class LocationProperty130(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_130'

class LocationProperty131(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_131'

class LocationProperty132(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_132'

class LocationProperty133(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_133'

class LocationProperty134(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_134'

class LocationProperty135(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_135'

class LocationProperty136(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_136'

class LocationProperty137(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_137'

class LocationProperty138(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_138'

class LocationProperty139(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_139'

class LocationProperty14(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_14'

class LocationProperty140(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_140'

class LocationProperty141(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_141'

class LocationProperty142(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_142'

class LocationProperty143(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_143'

class LocationProperty144(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_144'

class LocationProperty145(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_145'

class LocationProperty146(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_146'

class LocationProperty147(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_147'

class LocationProperty148(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_148'

class LocationProperty149(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_149'

class LocationProperty15(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_15'

class LocationProperty150(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_150'

class LocationProperty151(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_151'

class LocationProperty152(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_152'

class LocationProperty153(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_153'

class LocationProperty154(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_154'

class LocationProperty155(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_155'

class LocationProperty156(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_156'

class LocationProperty157(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_157'

class LocationProperty158(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_158'

class LocationProperty159(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_159'

class LocationProperty16(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_16'

class LocationProperty160(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_160'

class LocationProperty161(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_161'

class LocationProperty162(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_162'

class LocationProperty163(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_163'

class LocationProperty164(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_164'

class LocationProperty165(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_165'

class LocationProperty166(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_166'

class LocationProperty167(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_167'

class LocationProperty168(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_168'

class LocationProperty169(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_169'

class LocationProperty17(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_17'

class LocationProperty170(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_170'

class LocationProperty171(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_171'

class LocationProperty172(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_172'

class LocationProperty173(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_173'

class LocationProperty174(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_174'

class LocationProperty175(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_175'

class LocationProperty176(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_176'

class LocationProperty177(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_177'

class LocationProperty178(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_178'

class LocationProperty179(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_179'

class LocationProperty18(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_18'

class LocationProperty180(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_180'

class LocationProperty181(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_181'

class LocationProperty182(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_182'

class LocationProperty183(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_183'

class LocationProperty184(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_184'

class LocationProperty185(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_185'

class LocationProperty186(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_186'

class LocationProperty187(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_187'

class LocationProperty188(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_188'

class LocationProperty189(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_189'

class LocationProperty19(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_19'

class LocationProperty190(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_190'

class LocationProperty191(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_191'

class LocationProperty192(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_192'

class LocationProperty193(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_193'

class LocationProperty194(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_194'

class LocationProperty195(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_195'

class LocationProperty196(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_196'

class LocationProperty197(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_197'

class LocationProperty198(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_198'

class LocationProperty199(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_199'

class LocationProperty2(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_2'

class LocationProperty20(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_20'

class LocationProperty200(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_200'

class LocationProperty201(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_201'

class LocationProperty202(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_202'

class LocationProperty203(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_203'

class LocationProperty204(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_204'

class LocationProperty205(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_205'

class LocationProperty206(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_206'

class LocationProperty207(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_207'

class LocationProperty208(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_208'

class LocationProperty209(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_209'

class LocationProperty21(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_21'

class LocationProperty210(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_210'

class LocationProperty211(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_211'

class LocationProperty212(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_212'

class LocationProperty213(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_213'

class LocationProperty214(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_214'

class LocationProperty215(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_215'

class LocationProperty216(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_216'

class LocationProperty217(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_217'

class LocationProperty218(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_218'

class LocationProperty219(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_219'

class LocationProperty22(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_22'

class LocationProperty220(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_220'

class LocationProperty221(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_221'

class LocationProperty222(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_222'

class LocationProperty223(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_223'

class LocationProperty224(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_224'

class LocationProperty225(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_225'

class LocationProperty226(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_226'

class LocationProperty227(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_227'

class LocationProperty228(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_228'

class LocationProperty229(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_229'

class LocationProperty23(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_23'

class LocationProperty230(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_230'

class LocationProperty231(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_231'

class LocationProperty232(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_232'

class LocationProperty233(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_233'

class LocationProperty234(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_234'

class LocationProperty235(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_235'

class LocationProperty236(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_236'

class LocationProperty237(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_237'

class LocationProperty238(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_238'

class LocationProperty239(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_239'

class LocationProperty24(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_24'

class LocationProperty240(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_240'

class LocationProperty241(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_241'

class LocationProperty242(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_242'

class LocationProperty243(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_243'

class LocationProperty244(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_244'

class LocationProperty245(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_245'

class LocationProperty246(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_246'

class LocationProperty247(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_247'

class LocationProperty248(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_248'

class LocationProperty249(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_249'

class LocationProperty25(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_25'

class LocationProperty250(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_250'

class LocationProperty26(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_26'

class LocationProperty27(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_27'

class LocationProperty28(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_28'

class LocationProperty29(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_29'

class LocationProperty3(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_3'

class LocationProperty30(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_30'

class LocationProperty31(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_31'

class LocationProperty32(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_32'

class LocationProperty33(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_33'

class LocationProperty34(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_34'

class LocationProperty35(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_35'

class LocationProperty36(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_36'

class LocationProperty37(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_37'

class LocationProperty38(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_38'

class LocationProperty39(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_39'

class LocationProperty4(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_4'

class LocationProperty40(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_40'

class LocationProperty41(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_41'

class LocationProperty42(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_42'

class LocationProperty43(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_43'

class LocationProperty44(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_44'

class LocationProperty45(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_45'

class LocationProperty46(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_46'

class LocationProperty47(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_47'

class LocationProperty48(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_48'

class LocationProperty49(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_49'

class LocationProperty5(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_5'

class LocationProperty50(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_50'

class LocationProperty51(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_51'

class LocationProperty52(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_52'

class LocationProperty53(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_53'

class LocationProperty54(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_54'

class LocationProperty55(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_55'

class LocationProperty56(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_56'

class LocationProperty57(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_57'

class LocationProperty58(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_58'

class LocationProperty59(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_59'

class LocationProperty6(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_6'

class LocationProperty60(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_60'

class LocationProperty61(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_61'

class LocationProperty62(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_62'

class LocationProperty63(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_63'

class LocationProperty64(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_64'

class LocationProperty65(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_65'

class LocationProperty66(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_66'

class LocationProperty67(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_67'

class LocationProperty68(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_68'

class LocationProperty69(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_69'

class LocationProperty7(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_7'

class LocationProperty70(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_70'

class LocationProperty71(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_71'

class LocationProperty72(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_72'

class LocationProperty73(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_73'

class LocationProperty74(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_74'

class LocationProperty75(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_75'

class LocationProperty76(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_76'

class LocationProperty77(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_77'

class LocationProperty78(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_78'

class LocationProperty79(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_79'

class LocationProperty8(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_8'

class LocationProperty80(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_80'

class LocationProperty81(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_81'

class LocationProperty82(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_82'

class LocationProperty83(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_83'

class LocationProperty84(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_84'

class LocationProperty85(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_85'

class LocationProperty86(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_86'

class LocationProperty87(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_87'

class LocationProperty88(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_88'

class LocationProperty89(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_89'

class LocationProperty9(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_9'

class LocationProperty90(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_90'

class LocationProperty91(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_91'

class LocationProperty92(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_92'

class LocationProperty93(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_93'

class LocationProperty94(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_94'

class LocationProperty95(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_95'

class LocationProperty96(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_96'

class LocationProperty97(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_97'

class LocationProperty98(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_98'

class LocationProperty99(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_99'

class LocationPropertyAux(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_aux'

class LocationPropertyTiger(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    partition = models.IntegerField(null=True, blank=True)
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_property_tiger'

class LocationRoad0(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_0'

class LocationRoad1(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_1'

class LocationRoad10(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_10'

class LocationRoad100(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_100'

class LocationRoad101(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_101'

class LocationRoad102(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_102'

class LocationRoad103(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_103'

class LocationRoad104(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_104'

class LocationRoad105(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_105'

class LocationRoad106(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_106'

class LocationRoad107(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_107'

class LocationRoad108(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_108'

class LocationRoad109(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_109'

class LocationRoad11(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_11'

class LocationRoad110(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_110'

class LocationRoad111(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_111'

class LocationRoad112(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_112'

class LocationRoad113(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_113'

class LocationRoad114(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_114'

class LocationRoad115(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_115'

class LocationRoad116(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_116'

class LocationRoad117(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_117'

class LocationRoad118(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_118'

class LocationRoad119(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_119'

class LocationRoad12(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_12'

class LocationRoad120(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_120'

class LocationRoad121(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_121'

class LocationRoad122(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_122'

class LocationRoad123(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_123'

class LocationRoad124(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_124'

class LocationRoad125(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_125'

class LocationRoad126(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_126'

class LocationRoad127(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_127'

class LocationRoad128(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_128'

class LocationRoad129(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_129'

class LocationRoad13(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_13'

class LocationRoad130(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_130'

class LocationRoad131(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_131'

class LocationRoad132(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_132'

class LocationRoad133(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_133'

class LocationRoad134(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_134'

class LocationRoad135(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_135'

class LocationRoad136(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_136'

class LocationRoad137(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_137'

class LocationRoad138(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_138'

class LocationRoad139(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_139'

class LocationRoad14(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_14'

class LocationRoad140(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_140'

class LocationRoad141(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_141'

class LocationRoad142(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_142'

class LocationRoad143(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_143'

class LocationRoad144(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_144'

class LocationRoad145(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_145'

class LocationRoad146(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_146'

class LocationRoad147(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_147'

class LocationRoad148(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_148'

class LocationRoad149(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_149'

class LocationRoad15(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_15'

class LocationRoad150(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_150'

class LocationRoad151(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_151'

class LocationRoad152(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_152'

class LocationRoad153(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_153'

class LocationRoad154(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_154'

class LocationRoad155(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_155'

class LocationRoad156(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_156'

class LocationRoad157(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_157'

class LocationRoad158(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_158'

class LocationRoad159(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_159'

class LocationRoad16(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_16'

class LocationRoad160(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_160'

class LocationRoad161(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_161'

class LocationRoad162(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_162'

class LocationRoad163(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_163'

class LocationRoad164(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_164'

class LocationRoad165(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_165'

class LocationRoad166(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_166'

class LocationRoad167(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_167'

class LocationRoad168(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_168'

class LocationRoad169(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_169'

class LocationRoad17(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_17'

class LocationRoad170(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_170'

class LocationRoad171(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_171'

class LocationRoad172(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_172'

class LocationRoad173(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_173'

class LocationRoad174(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_174'

class LocationRoad175(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_175'

class LocationRoad176(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_176'

class LocationRoad177(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_177'

class LocationRoad178(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_178'

class LocationRoad179(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_179'

class LocationRoad18(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_18'

class LocationRoad180(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_180'

class LocationRoad181(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_181'

class LocationRoad182(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_182'

class LocationRoad183(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_183'

class LocationRoad184(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_184'

class LocationRoad185(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_185'

class LocationRoad186(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_186'

class LocationRoad187(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_187'

class LocationRoad188(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_188'

class LocationRoad189(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_189'

class LocationRoad19(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_19'

class LocationRoad190(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_190'

class LocationRoad191(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_191'

class LocationRoad192(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_192'

class LocationRoad193(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_193'

class LocationRoad194(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_194'

class LocationRoad195(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_195'

class LocationRoad196(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_196'

class LocationRoad197(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_197'

class LocationRoad198(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_198'

class LocationRoad199(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_199'

class LocationRoad2(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_2'

class LocationRoad20(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_20'

class LocationRoad200(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_200'

class LocationRoad201(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_201'

class LocationRoad202(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_202'

class LocationRoad203(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_203'

class LocationRoad204(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_204'

class LocationRoad205(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_205'

class LocationRoad206(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_206'

class LocationRoad207(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_207'

class LocationRoad208(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_208'

class LocationRoad209(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_209'

class LocationRoad21(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_21'

class LocationRoad210(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_210'

class LocationRoad211(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_211'

class LocationRoad212(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_212'

class LocationRoad213(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_213'

class LocationRoad214(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_214'

class LocationRoad215(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_215'

class LocationRoad216(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_216'

class LocationRoad217(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_217'

class LocationRoad218(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_218'

class LocationRoad219(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_219'

class LocationRoad22(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_22'

class LocationRoad220(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_220'

class LocationRoad221(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_221'

class LocationRoad222(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_222'

class LocationRoad223(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_223'

class LocationRoad224(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_224'

class LocationRoad225(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_225'

class LocationRoad226(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_226'

class LocationRoad227(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_227'

class LocationRoad228(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_228'

class LocationRoad229(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_229'

class LocationRoad23(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_23'

class LocationRoad230(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_230'

class LocationRoad231(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_231'

class LocationRoad232(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_232'

class LocationRoad233(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_233'

class LocationRoad234(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_234'

class LocationRoad235(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_235'

class LocationRoad236(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_236'

class LocationRoad237(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_237'

class LocationRoad238(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_238'

class LocationRoad239(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_239'

class LocationRoad24(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_24'

class LocationRoad240(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_240'

class LocationRoad241(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_241'

class LocationRoad242(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_242'

class LocationRoad243(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_243'

class LocationRoad244(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_244'

class LocationRoad245(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_245'

class LocationRoad246(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_246'

class LocationRoad247(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_247'

class LocationRoad248(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_248'

class LocationRoad249(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_249'

class LocationRoad25(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_25'

class LocationRoad250(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_250'

class LocationRoad26(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_26'

class LocationRoad27(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_27'

class LocationRoad28(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_28'

class LocationRoad29(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_29'

class LocationRoad3(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_3'

class LocationRoad30(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_30'

class LocationRoad31(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_31'

class LocationRoad32(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_32'

class LocationRoad33(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_33'

class LocationRoad34(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_34'

class LocationRoad35(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_35'

class LocationRoad36(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_36'

class LocationRoad37(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_37'

class LocationRoad38(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_38'

class LocationRoad39(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_39'

class LocationRoad4(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_4'

class LocationRoad40(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_40'

class LocationRoad41(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_41'

class LocationRoad42(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_42'

class LocationRoad43(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_43'

class LocationRoad44(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_44'

class LocationRoad45(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_45'

class LocationRoad46(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_46'

class LocationRoad47(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_47'

class LocationRoad48(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_48'

class LocationRoad49(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_49'

class LocationRoad5(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_5'

class LocationRoad50(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_50'

class LocationRoad51(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_51'

class LocationRoad52(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_52'

class LocationRoad53(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_53'

class LocationRoad54(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_54'

class LocationRoad55(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_55'

class LocationRoad56(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_56'

class LocationRoad57(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_57'

class LocationRoad58(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_58'

class LocationRoad59(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_59'

class LocationRoad6(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_6'

class LocationRoad60(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_60'

class LocationRoad61(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_61'

class LocationRoad62(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_62'

class LocationRoad63(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_63'

class LocationRoad64(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_64'

class LocationRoad65(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_65'

class LocationRoad66(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_66'

class LocationRoad67(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_67'

class LocationRoad68(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_68'

class LocationRoad69(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_69'

class LocationRoad7(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_7'

class LocationRoad70(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_70'

class LocationRoad71(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_71'

class LocationRoad72(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_72'

class LocationRoad73(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_73'

class LocationRoad74(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_74'

class LocationRoad75(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_75'

class LocationRoad76(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_76'

class LocationRoad77(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_77'

class LocationRoad78(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_78'

class LocationRoad79(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_79'

class LocationRoad8(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_8'

class LocationRoad80(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_80'

class LocationRoad81(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_81'

class LocationRoad82(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_82'

class LocationRoad83(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_83'

class LocationRoad84(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_84'

class LocationRoad85(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_85'

class LocationRoad86(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_86'

class LocationRoad87(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_87'

class LocationRoad88(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_88'

class LocationRoad89(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_89'

class LocationRoad9(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_9'

class LocationRoad90(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_90'

class LocationRoad91(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_91'

class LocationRoad92(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_92'

class LocationRoad93(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_93'

class LocationRoad94(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_94'

class LocationRoad95(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_95'

class LocationRoad96(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_96'

class LocationRoad97(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_97'

class LocationRoad98(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_98'

class LocationRoad99(models.Model):
    partition = models.IntegerField(null=True, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    geometry = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'location_road_99'

class NewQueryLog(models.Model):
    type = models.TextField(blank=True)
    starttime = models.DateTimeField(null=True, blank=True)
    ipaddress = models.TextField(blank=True)
    useragent = models.TextField(blank=True)
    language = models.TextField(blank=True)
    query = models.TextField(blank=True)
    endtime = models.DateTimeField(null=True, blank=True)
    results = models.IntegerField(null=True, blank=True)
    format = models.TextField(blank=True)
    secret = models.TextField(blank=True)
    class Meta:
        db_table = 'new_query_log'

class Place(models.Model):
    osm_type = models.CharField(max_length=1)
    osm_id = models.IntegerField()
    class_field = models.TextField(db_column='class') # Field renamed because it was a Python reserved word.
    type = models.TextField()
    name = models.TextField(blank=True) # This field type is a guess.
    admin_level = models.IntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    street = models.TextField(blank=True)
    isin = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    extratags = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField() # This field type is a guess.
    class Meta:
        db_table = 'place'

class PlaceAddressline(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    address_place_id = models.BigIntegerField(null=True, blank=True)
    fromarea = models.BooleanField(null=True, blank=True)
    isaddress = models.BooleanField(null=True, blank=True)
    distance = models.FloatField(null=True, blank=True)
    cached_rank_address = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'place_addressline'

class PlaceBoundingbox(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    minlat = models.FloatField(null=True, blank=True)
    maxlat = models.FloatField(null=True, blank=True)
    minlon = models.FloatField(null=True, blank=True)
    maxlon = models.FloatField(null=True, blank=True)
    numfeatures = models.IntegerField(null=True, blank=True)
    area = models.FloatField(null=True, blank=True)
    outline = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'place_boundingbox'

class Placex(models.Model):
    place_id = models.BigIntegerField(unique=True)
    partition = models.IntegerField(null=True, blank=True)
    osm_type = models.CharField(max_length=1)
    osm_id = models.IntegerField()
    class_field = models.TextField(db_column='class') # Field renamed because it was a Python reserved word.
    type = models.TextField()
    name = models.TextField(blank=True) # This field type is a guess.
    admin_level = models.IntegerField(null=True, blank=True)
    housenumber = models.TextField(blank=True)
    street = models.TextField(blank=True)
    isin = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    extratags = models.TextField(blank=True) # This field type is a guess.
    geometry = models.TextField() # This field type is a guess.
    parent_place_id = models.BigIntegerField(null=True, blank=True)
    linked_place_id = models.BigIntegerField(null=True, blank=True)
    rank_address = models.IntegerField(null=True, blank=True)
    rank_search = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    indexed_status = models.IntegerField(null=True, blank=True)
    indexed_date = models.DateTimeField(null=True, blank=True)
    wikipedia = models.TextField(blank=True)
    geometry_sector = models.IntegerField(null=True, blank=True)
    calculated_country_code = models.CharField(max_length=2, blank=True)
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'placex'

class PlanetOsmNodes(models.Model):
    id = models.IntegerField(primary_key=True)
    lat = models.IntegerField()
    lon = models.IntegerField()
    tags = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'planet_osm_nodes'

class PlanetOsmRels(models.Model):
    id = models.IntegerField(primary_key=True)
    way_off = models.SmallIntegerField(null=True, blank=True)
    rel_off = models.SmallIntegerField(null=True, blank=True)
    parts = models.TextField(blank=True) # This field type is a guess.
    members = models.TextField(blank=True) # This field type is a guess.
    tags = models.TextField(blank=True) # This field type is a guess.
    pending = models.BooleanField()
    class Meta:
        db_table = 'planet_osm_rels'

class PlanetOsmWays(models.Model):
    id = models.IntegerField(primary_key=True)
    nodes = models.TextField() # This field type is a guess.
    tags = models.TextField(blank=True) # This field type is a guess.
    pending = models.BooleanField()
    class Meta:
        db_table = 'planet_osm_ways'

class QueryLog(models.Model):
    starttime = models.DateTimeField(null=True, blank=True)
    query = models.TextField(blank=True)
    ipaddress = models.TextField(blank=True)
    endtime = models.DateTimeField(null=True, blank=True)
    results = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'query_log'

class ReportLog(models.Model):
    starttime = models.DateTimeField(null=True, blank=True)
    ipaddress = models.TextField(blank=True)
    query = models.TextField(blank=True)
    description = models.TextField(blank=True)
    email = models.TextField(blank=True)
    class Meta:
        db_table = 'report_log'

class ReverseCache(models.Model):
    latlonzoomid = models.IntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    place_id = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = 'reverse_cache'

class SearchName(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name'

class SearchName0(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_0'

class SearchName1(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_1'

class SearchName10(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_10'

class SearchName100(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_100'

class SearchName101(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_101'

class SearchName102(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_102'

class SearchName103(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_103'

class SearchName104(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_104'

class SearchName105(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_105'

class SearchName106(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_106'

class SearchName107(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_107'

class SearchName108(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_108'

class SearchName109(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_109'

class SearchName11(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_11'

class SearchName110(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_110'

class SearchName111(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_111'

class SearchName112(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_112'

class SearchName113(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_113'

class SearchName114(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_114'

class SearchName115(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_115'

class SearchName116(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_116'

class SearchName117(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_117'

class SearchName118(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_118'

class SearchName119(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_119'

class SearchName12(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_12'

class SearchName120(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_120'

class SearchName121(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_121'

class SearchName122(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_122'

class SearchName123(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_123'

class SearchName124(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_124'

class SearchName125(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_125'

class SearchName126(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_126'

class SearchName127(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_127'

class SearchName128(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_128'

class SearchName129(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_129'

class SearchName13(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_13'

class SearchName130(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_130'

class SearchName131(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_131'

class SearchName132(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_132'

class SearchName133(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_133'

class SearchName134(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_134'

class SearchName135(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_135'

class SearchName136(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_136'

class SearchName137(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_137'

class SearchName138(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_138'

class SearchName139(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_139'

class SearchName14(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_14'

class SearchName140(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_140'

class SearchName141(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_141'

class SearchName142(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_142'

class SearchName143(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_143'

class SearchName144(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_144'

class SearchName145(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_145'

class SearchName146(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_146'

class SearchName147(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_147'

class SearchName148(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_148'

class SearchName149(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_149'

class SearchName15(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_15'

class SearchName150(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_150'

class SearchName151(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_151'

class SearchName152(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_152'

class SearchName153(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_153'

class SearchName154(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_154'

class SearchName155(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_155'

class SearchName156(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_156'

class SearchName157(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_157'

class SearchName158(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_158'

class SearchName159(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_159'

class SearchName16(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_16'

class SearchName160(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_160'

class SearchName161(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_161'

class SearchName162(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_162'

class SearchName163(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_163'

class SearchName164(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_164'

class SearchName165(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_165'

class SearchName166(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_166'

class SearchName167(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_167'

class SearchName168(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_168'

class SearchName169(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_169'

class SearchName17(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_17'

class SearchName170(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_170'

class SearchName171(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_171'

class SearchName172(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_172'

class SearchName173(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_173'

class SearchName174(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_174'

class SearchName175(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_175'

class SearchName176(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_176'

class SearchName177(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_177'

class SearchName178(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_178'

class SearchName179(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_179'

class SearchName18(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_18'

class SearchName180(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_180'

class SearchName181(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_181'

class SearchName182(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_182'

class SearchName183(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_183'

class SearchName184(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_184'

class SearchName185(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_185'

class SearchName186(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_186'

class SearchName187(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_187'

class SearchName188(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_188'

class SearchName189(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_189'

class SearchName19(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_19'

class SearchName190(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_190'

class SearchName191(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_191'

class SearchName192(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_192'

class SearchName193(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_193'

class SearchName194(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_194'

class SearchName195(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_195'

class SearchName196(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_196'

class SearchName197(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_197'

class SearchName198(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_198'

class SearchName199(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_199'

class SearchName2(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_2'

class SearchName20(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_20'

class SearchName200(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_200'

class SearchName201(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_201'

class SearchName202(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_202'

class SearchName203(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_203'

class SearchName204(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_204'

class SearchName205(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_205'

class SearchName206(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_206'

class SearchName207(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_207'

class SearchName208(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_208'

class SearchName209(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_209'

class SearchName21(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_21'

class SearchName210(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_210'

class SearchName211(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_211'

class SearchName212(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_212'

class SearchName213(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_213'

class SearchName214(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_214'

class SearchName215(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_215'

class SearchName216(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_216'

class SearchName217(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_217'

class SearchName218(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_218'

class SearchName219(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_219'

class SearchName22(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_22'

class SearchName220(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_220'

class SearchName221(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_221'

class SearchName222(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_222'

class SearchName223(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_223'

class SearchName224(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_224'

class SearchName225(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_225'

class SearchName226(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_226'

class SearchName227(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_227'

class SearchName228(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_228'

class SearchName229(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_229'

class SearchName23(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_23'

class SearchName230(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_230'

class SearchName231(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_231'

class SearchName232(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_232'

class SearchName233(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_233'

class SearchName234(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_234'

class SearchName235(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_235'

class SearchName236(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_236'

class SearchName237(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_237'

class SearchName238(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_238'

class SearchName239(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_239'

class SearchName24(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_24'

class SearchName240(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_240'

class SearchName241(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_241'

class SearchName242(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_242'

class SearchName243(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_243'

class SearchName244(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_244'

class SearchName245(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_245'

class SearchName246(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_246'

class SearchName247(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_247'

class SearchName248(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_248'

class SearchName249(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_249'

class SearchName25(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_25'

class SearchName250(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_250'

class SearchName26(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_26'

class SearchName27(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_27'

class SearchName28(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_28'

class SearchName29(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_29'

class SearchName3(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_3'

class SearchName30(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_30'

class SearchName31(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_31'

class SearchName32(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_32'

class SearchName33(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_33'

class SearchName34(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_34'

class SearchName35(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_35'

class SearchName36(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_36'

class SearchName37(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_37'

class SearchName38(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_38'

class SearchName39(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_39'

class SearchName4(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_4'

class SearchName40(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_40'

class SearchName41(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_41'

class SearchName42(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_42'

class SearchName43(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_43'

class SearchName44(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_44'

class SearchName45(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_45'

class SearchName46(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_46'

class SearchName47(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_47'

class SearchName48(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_48'

class SearchName49(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_49'

class SearchName5(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_5'

class SearchName50(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_50'

class SearchName51(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_51'

class SearchName52(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_52'

class SearchName53(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_53'

class SearchName54(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_54'

class SearchName55(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_55'

class SearchName56(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_56'

class SearchName57(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_57'

class SearchName58(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_58'

class SearchName59(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_59'

class SearchName6(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_6'

class SearchName60(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_60'

class SearchName61(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_61'

class SearchName62(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_62'

class SearchName63(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_63'

class SearchName64(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_64'

class SearchName65(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_65'

class SearchName66(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_66'

class SearchName67(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_67'

class SearchName68(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_68'

class SearchName69(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_69'

class SearchName7(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_7'

class SearchName70(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_70'

class SearchName71(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_71'

class SearchName72(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_72'

class SearchName73(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_73'

class SearchName74(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_74'

class SearchName75(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_75'

class SearchName76(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_76'

class SearchName77(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_77'

class SearchName78(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_78'

class SearchName79(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_79'

class SearchName8(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_8'

class SearchName80(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_80'

class SearchName81(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_81'

class SearchName82(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_82'

class SearchName83(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_83'

class SearchName84(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_84'

class SearchName85(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_85'

class SearchName86(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_86'

class SearchName87(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_87'

class SearchName88(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_88'

class SearchName89(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_89'

class SearchName9(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_9'

class SearchName90(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_90'

class SearchName91(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_91'

class SearchName92(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_92'

class SearchName93(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_93'

class SearchName94(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_94'

class SearchName95(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_95'

class SearchName96(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_96'

class SearchName97(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_97'

class SearchName98(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_98'

class SearchName99(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_99'

class SearchNameBlank(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_blank'

class SearchNameCountry(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    search_rank = models.IntegerField(null=True, blank=True)
    address_rank = models.IntegerField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    name_vector = models.TextField(blank=True) # This field type is a guess.
    nameaddress_vector = models.TextField(blank=True) # This field type is a guess.
    centroid = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'search_name_country'

class SpatialRefSys(models.Model):
    srid = models.IntegerField(primary_key=True)
    auth_name = models.CharField(max_length=256, blank=True)
    auth_srid = models.IntegerField(null=True, blank=True)
    srtext = models.CharField(max_length=2048, blank=True)
    proj4text = models.CharField(max_length=2048, blank=True)
    class Meta:
        db_table = 'spatial_ref_sys'

class UsPostcode(models.Model):
    postcode = models.TextField(blank=True)
    x = models.FloatField(null=True, blank=True)
    y = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = 'us_postcode'

class UsState(models.Model):
    gid = models.IntegerField(primary_key=True)
    area = models.FloatField(null=True, blank=True)
    perimeter = models.FloatField(null=True, blank=True)
    statesp020 = models.BigIntegerField(null=True, blank=True)
    state = models.CharField(max_length=20, blank=True)
    state_fips = models.CharField(max_length=2, blank=True)
    order_adm = models.IntegerField(null=True, blank=True)
    month_adm = models.CharField(max_length=18, blank=True)
    day_adm = models.BigIntegerField(null=True, blank=True)
    year_adm = models.BigIntegerField(null=True, blank=True)
    the_geom = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'us_state'

class UsStatecounty(models.Model):
    gid = models.IntegerField(primary_key=True)
    area = models.FloatField(null=True, blank=True)
    perimeter = models.FloatField(null=True, blank=True)
    countyp020 = models.BigIntegerField(null=True, blank=True)
    state = models.CharField(max_length=2, blank=True)
    county = models.CharField(max_length=50, blank=True)
    fips = models.CharField(max_length=5, blank=True)
    state_fips = models.CharField(max_length=2, blank=True)
    square_mil = models.FloatField(null=True, blank=True)
    the_geom = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'us_statecounty'

class VwSearchQueryLog(models.Model):
    query = models.TextField(blank=True)
    starttime = models.DateTimeField(null=True, blank=True)
    duration = models.TextField(blank=True) # This field type is a guess.
    useragent = models.TextField(blank=True)
    language = models.TextField(blank=True)
    results = models.IntegerField(null=True, blank=True)
    ipaddress = models.TextField(blank=True)
    class Meta:
        db_table = 'vw_search_query_log'

class WikipediaArticle(models.Model):
    language = models.TextField()
    title = models.TextField()
    langcount = models.IntegerField(null=True, blank=True)
    othercount = models.IntegerField(null=True, blank=True)
    totalcount = models.IntegerField(null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    osm_type = models.CharField(max_length=1, blank=True)
    osm_id = models.BigIntegerField(null=True, blank=True)
    infobox_type = models.TextField(blank=True)
    population = models.BigIntegerField(null=True, blank=True)
    website = models.TextField(blank=True)
    class Meta:
        db_table = 'wikipedia_article'

class WikipediaRedirect(models.Model):
    language = models.TextField(blank=True)
    from_title = models.TextField(blank=True)
    to_title = models.TextField(blank=True)
    class Meta:
        db_table = 'wikipedia_redirect'

class Word(models.Model):
    word_id = models.IntegerField(null=True, blank=True)
    word_token = models.TextField(blank=True)
    word_trigram = models.TextField(blank=True)
    word = models.TextField(blank=True)
    class_field = models.TextField(db_column='class', blank=True) # Field renamed because it was a Python reserved word.
    type = models.TextField(blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    search_name_count = models.IntegerField(null=True, blank=True)
    operator = models.TextField(blank=True)
    location = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'word'

class Worldboundaries(models.Model):
    gid = models.IntegerField(primary_key=True)
    cat = models.BigIntegerField(null=True, blank=True)
    fips_cntry = models.CharField(max_length=80, blank=True)
    cntry_name = models.CharField(max_length=80, blank=True)
    the_geom = models.TextField(blank=True) # This field type is a guess.
    iso3166 = models.CharField(max_length=2, blank=True)
    class Meta:
        db_table = 'worldboundaries'

