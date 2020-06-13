# parcels/api/views.py

from ..models import ParcelInfo, History
from . import serializers
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


## Parcel 

class ParcelListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,) 
    queryset = ParcelInfo.objects.all()
    serializer_class = serializers.ParcelSerializer

class ParcelCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,) 
    queryset = ParcelInfo.objects.all()
    serializer_class = serializers.ParcelSerializer

    def create(self, request, *args, **kwargs):
        super(ParcelCreateView, self).create(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully created",
                    "result": request.data}
        return Response(response)
    
class ParcelDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,) 
    queryset = ParcelInfo.objects.all()
    serializer_class = serializers.ParcelSerializer
    
    def retrieve(self, request, *args, **kwargs):
        super(ParcelDetailView, self).retrieve(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully retrieved",
                    "result": data}
        return Response(response)

    def patch(self, request, *args, **kwargs):
        super(ParcelDetailView, self).patch(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully updated",
                    "result": data}
        return Response(response)

    def delete(self, request, *args, **kwargs):
        super(ParcelDetailView, self).delete(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully deleted"}
        return Response(response)

# History
class HistoryListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,) 
    queryset = History.objects.all()
    serializer_class = serializers.HistorySerializer

class HistoryCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,) 
    queryset = History.objects.all()
    serializer_class = serializers.HistorySerializer

    def create(self, request, *args, **kwargs):
        super(HistoryCreateView, self).create(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully created",
                    "result": request.data}
        return Response(response)
    
class HistoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,) 
    queryset = History.objects.all()
    serializer_class = serializers.HistorySerializer
    
    def retrieve(self, request, *args, **kwargs):
        super(HistoryDetailView, self).retrieve(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully retrieved",
                    "result": data}
        return Response(response)

    def patch(self, request, *args, **kwargs):
        super(HistoryDetailView, self).patch(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully updated",
                    "result": data}
        return Response(response)

    def delete(self, request, *args, **kwargs):
        super(HistoryDetailView, self).delete(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully deleted"}
        return Response(response)
