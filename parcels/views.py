from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import ParcelSpot


def get_top_100(lat,long):
    return 'something'