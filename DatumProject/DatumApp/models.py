from django.contrib.gis.db import models


# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Object(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=40)
    geo_coord = models.PointField()
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
