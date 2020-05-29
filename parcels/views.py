from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import ParcelInfo
import geopy
from  geopy.geocoders import Nominatim
from django.views.generic import ListView

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


class EntryList(ListView): 
    queryset = ParcelInfo.objects.filter(planno__isnull=False)
    
    