from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import ParcelInfo, History
from  geopy.geocoders import Nominatim
import geopy
import json

def get_lat_long(request):
    if request.GET.get('location'):
            address = request.GET.get('location')
            try:
                locator = Nominatim(user_agent="myGeocoder")
                location = locator.geocode(address)
                print(location)
                #do something with user
                html = ("<H1>%s</H1>", location)
                return render(request, 'index.html',{
                'address': location[0],
                'coordinates': location[1],
                'lat': location[1][0],
                'long': location[1][1],
                'html': html,
            })
            except:
                return render(request, 'index.html')
    else:
        return render(request, 'index.html')
    
def get_top_100(lat,long):
    return 'something'

def parcel_info(request):
    parcelz=serialize('geojson',ParcelInfo.objects.all())
    trial = json.loads(parcelz)
    for i in trial['features']: 
        filteri = i['properties']['planid']
        queryset = serialize('json',History.objects.filter(planid=filteri))
        if len(queryset) > 0:
            break
    return HttpResponse(queryset,content_type='json')

def parcel_details(request): 
    queryset = serialize('json',History.objects.all())
    return HttpResponse(queryset,content_type='json')