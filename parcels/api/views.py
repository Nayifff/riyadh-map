# parcels/api/views.py

from ..models import ParcelInfo, History
from . import serializers
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class ParcelListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,) 
    queryset = ParcelInfo.objects.all()
    serializer_class = serializers.ParcelSerializer
    
    def create(self, request, *args, **kwargs):
        super(ParcelListView, self).create(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully created",
                    "result": request.data}
        return Response(response)