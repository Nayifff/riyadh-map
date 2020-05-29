#from djgeojson.fields import PolygonField
from django.db import models
from django.contrib.gis.db import models as gismodels


class ParcelInfo(models.Model):

    planid = models.CharField(max_length=256, default=0)
    planno = models.CharField(max_length=256, default=0)
    parcelno = models.CharField(max_length=256, default=0)
    geom = gismodels.PolygonField()
    lat = models.CharField(max_length=256, default=0)
    long = models.CharField(max_length=256, default=0)
    area = models.CharField(max_length=256, default=0)

    def __str__(self):
        return self.planid

#class History(models.Model):
#
#    id_ = models.CharField(max_length=256)
#    description = models.TextField()
#    price = []
#    date = []
#    geom = PolygonField()
#
#    def __str__(self):
#        return self.title
#
#
#import pandas as pd
##from models import ParcelInfo
#df=pd.read_csv('parcels/db_sample.csv')
##
###print(df)
##
#row_iter = df.iterrows()
#
#for row in row_iter:
#    planid = row['id'],
#    planno  = row['planno'],
#    parcelno  = row['parcelno'],
#    coords  = row['coords'],
#    lat  = row['lat'],
#    long  = row['long'],
#    area  = row['area']
#    ParcelInfo(planid=planid, planno=planno, parcelno=parcelno, coords=coords,lat=lat,long=long,area=area).save()