from ..models import ParcelInfo, History 
from rest_framework import serializers

class ParcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParcelInfo
        fields = ('parcelid', 'planno', 'parcelno','geom','lat','long','area')
        
        
class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ('parcelid', 'description','neighborhood', 'price','date')
