from django.db import models
from django.contrib.gis.db import models as gismodels

# Create your models here.
# class WeatherStation(gismodels.Model):

#     wmoid = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=256)

#     geom = gismodels.PointField()

#     objects = gismodels.GeoManager()

#     def __unicode__(self):
#         return self.name

#     def dms2dex(value):
#         degres, minutes, seconds = value.split()
#         seconds, direction = seconds[:-1], seconds[-1]
#         dec = float(degres) + float(minutes)/60 + float(seconds)/3600
#         if direction in ('S', 'W'):
#             return -dec
#         return dec
#     #Degrees, Minutes, Seconds to Decimal degrees
    