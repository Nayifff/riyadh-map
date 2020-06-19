"""mushrooms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/stable/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView
from .views import *
from django.urls import path, include
from .api import views
from .models import ParcelInfo


urlpatterns = [
    url(r'^adminandonlyadmin/', admin.site.urls),
    url(r'^about/', about, name='about'),
#     url(r'^contact/$', contact, name='contact'),
    url(r'^analytics/', analytics, name='analytics'),
#     url(r'^data.geojson$', GeoJSONLayerView.as_view(model=ParcelInfo,        properties=('planno', 'parcelno', 'area')), name='data'),
#    url(r'^details.json/',parcel_details,name='details'),
    url(r'^(?P<lat>-?\d+.?\d+)/(?P<long>-?\d+.?\d+)/data.geojson$',parcel_info,name='data'),
    url('^contact/', contactView, name='contact'),
    url('success/', successView, name='success'),
    url(r'^rest-auth/', include('rest_auth.urls')),
    path('api/parcels', views.ParcelListView.as_view(), name=None),
    path('api/parcels/create/', views.ParcelCreateView.as_view(), name=None),
    path('api/parcels/<int:pk>/', views.ParcelDetailView.as_view(), name=None),
    path('api/history', views.HistoryListView.as_view(), name=None),
    path('api/history/create/', views.HistoryCreateView.as_view(), name=None),
    path('api/history/<int:pk>/', views.HistoryDetailView.as_view(), name=None),
    url(r'^$', get_lat_long, name='locationi')] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

 