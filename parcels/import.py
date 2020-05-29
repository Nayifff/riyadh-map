import pandas as pd
from models import ParcelInfo

df=pd.read_csv('parcels/db_sample.csv')
#
##print(df)
#
row_iter = df.iterrows()
#
objs = [

    ParcelInfo(

        planid = row['id'],

        planno  = row['planno'],

        parcelno  = row['parcelno'],

        geom  = row['coords'],
        
        lat  = row['lat'],
        
        long  = row['long'],
        
        area  = row['area']

    )

    for index, row in row_iter

]

ParcelInfo.objects.bulk_create(objs)
#
##Note: myClass_in_model: the class (i.e., the table you want to populate data from csv) we defined in Django model.py
##Note: field_1 to filed_4 are the fields you defined in your Django model.
#
##    planid = models.CharField(max_length=256, default=0)
##    planno = models.CharField(max_length=256, default=0)
##    parcelno = models.CharField(max_length=256, default=0)
##    coords = PolygonField()
##    lat = models.CharField(max_length=256, default=0)
##    long = models.CharField(max_length=256, default=0)
##    area = models.CharField(max_length=256, default=0)
#
#from models import ParcelInfo
##from django.db import transaction, models
##import pandas as pd
##from models import ParcelInfo
#
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