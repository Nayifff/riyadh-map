#from djgeojson.fields import PolygonField
from django.db import models
from django.contrib.gis.db import models as gismodels

# Database table for parcels info: 
class ParcelInfo(models.Model):

    parcelid = models.CharField(max_length=256, default=0)
    planno = models.CharField(max_length=256, default=0)
    parcelno = models.CharField(max_length=256, default=0)
    geom = gismodels.PolygonField()
    lat = models.CharField(max_length=256, default=0)
    long = models.CharField(max_length=256, default=0)
    area = models.CharField(max_length=256, default=0)

    def __str__(self):
        return self.planid

    
# Database table for parcels info: 
class History(models.Model):

    parcelid = models.CharField(max_length=256)
    description = models.CharField(max_length=256, default="residential")
    neighborhood = models.CharField(max_length=256)
    price = models.CharField(max_length=256)
    date = models.DateField()
    

    def __str__(self):
        return self.planid
