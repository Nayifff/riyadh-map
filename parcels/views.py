from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import ParcelSpot
import geopy
from  geopy.geocoders import Nominatim

def get_lat_long(request):
    if request.GET.get('location'):
            address = request.GET.get('location')
            try:
                locator = Nominatim(user_agent="myGeocoder")
                location = locator.geocode(address)
                print(location)
                #do something with user
                html = ("<H1>%s</H1>", location)
            except:
                location = 'HEY'
            return render(request, 'index.html',{
                'address': location[0],
                'coordinates': location[1],
                'html': html,
            })
    else:
        return render(request, 'index.html')
    
def get_top_100(lat,long):
    return 'something'