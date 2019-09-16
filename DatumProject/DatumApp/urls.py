from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('types', views.TypeViewSet)
router.register('objects', views.ObjectViewSet)
router.register('objects-geo', views.ObjectGeoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls'))
]
