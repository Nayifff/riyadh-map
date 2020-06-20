from django.contrib.auth.decorators import login_required
from django.contrib.gis.geos import Polygon, Point
from django.contrib.gis.measure import Distance  
from django.core.mail import send_mail, BadHeaderError
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.core.serializers import serialize
from django.http import HttpResponse
from .forms import ContactForm
from .models import ParcelInfo, History
from  geopy.geocoders import Nominatim
import geopy
import json
import re

# function to get lat and long from an adress inputed by user 
def get_lat_long(request):
    if request.GET.get('location'):
            address = request.GET.get('location')
            try:
                locator = Nominatim(user_agent="myGeocoder")
                location = locator.geocode(address)
                print(location)
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

    
# function to get all 
def parcel_info(request,**kwargs):

    lat = float(kwargs['lat'])
    lng = float(kwargs['long'])
    point = Point(lng, lat)
    radius = 0.7
    parcelz=serialize('geojson',ParcelInfo.objects.filter(geom__distance_lt=(point, Distance(km=radius))))
    trial = json.loads(parcelz)
    ids = [element['properties']['parcelid'] for element in trial['features']]
    print(ids)
    queryset = serialize('json',History.objects.filter(parcelid__in=ids).order_by('-date'))
    letsee = json.loads(queryset)
    print(letsee)
    for i in trial['features']:
        id_ = i['properties']['parcelid']
        i['properties']['history'] = [x for x in letsee if x['fields']['parcelid'] == id_]
        print(i['properties']['history'])
    print(trial)
#    print(queryset)
#    things = [json.loads(line) for line in f]
#    i['properties']['history'] = queryset
    new = json.dumps(trial)
    return HttpResponse(new,content_type='json')

def parcel_details(request): 
    queryset = serialize('json',History.objects.all())
    return HttpResponse(queryset,content_type='json')


def contact(request):
    return render(request,'contact.html')

def analytics(request):
    return render(request,'analytics.html')

def about(request):
    return render(request,'about.html')


def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "contact.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')