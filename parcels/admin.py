from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin

from . import models as parcels_models


admin.site.register(parcels_models.ParcelInfo, LeafletGeoAdmin)
