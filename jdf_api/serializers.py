from rest_framework import serializers

from jdf.models import Place, Phonetique


class PlaceSerializer(serializers.ModelSerializer):
    """
    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(PlaceSerializer, self).__init__(many=many, *args, **kwargs)
    """
    phonetic = serializers.RelatedField(many=True)
    
    class Meta:
        model = Place
        fields = ('osm_id', 'class_field', 'type', 'name')


class PhonetiqueSerializer(serializers.ModelSerializer):
    osm = PlaceSerializer(many=False)
    
    class Meta :
        model = Phonetique
        fields = ('nom','poids','osm')
        
