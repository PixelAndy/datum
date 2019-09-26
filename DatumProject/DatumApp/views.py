from rest_framework import viewsets
from .models import Type, Object
from .serializers import TypeSerializer, ObjectSerializer, ObjectGeoSerializer


class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class ObjectViewSet(viewsets.ModelViewSet):
    queryset = Object.objects.all()
    serializer_class = ObjectSerializer


class ObjectGeoViewSet(viewsets.ModelViewSet):
    queryset = Object.objects.all()
    serializer_class = ObjectGeoSerializer
