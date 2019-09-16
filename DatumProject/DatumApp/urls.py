from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('types', views.TypeViewSet)
router.register('objects', views.ObjectViewSet, base_name='object')
router.register('objects-geo', views.ObjectGeoViewSet, base_name='objects-geo')

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls'))
]
