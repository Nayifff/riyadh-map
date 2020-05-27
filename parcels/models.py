from djgeojson.fields import PolygonField
from django.db import models


class ParcelSpot(models.Model):

    title = models.CharField(max_length=256)
    description = models.TextField()
    price = []
    date = []
    geom = PolygonField()

    def __str__(self):
        return self.title

