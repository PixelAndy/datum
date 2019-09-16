from .models import Type, Object
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers


class TypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Type
        fields = ['id', 'name', 'description']


class ObjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Object
        fields = ['id', 'name', 'description', 'type', 'geo_coord']


class ObjectGeoSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Object
        geo_field = "geo_coord"
        fields = ['id', 'name', 'description', 'type', 'geo_coord']