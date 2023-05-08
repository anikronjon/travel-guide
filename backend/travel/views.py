from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import ListView, DetailView
from .models import *


class TourListView(ListView):
    model = TouristPlace


class HotelListView(ListView):
    model = Hotel


class RestaurantListView(ListView):
    model = Restaurant


def home(request):
    tourPlaces = TouristPlace.objects.all()
    hotels = Hotel.objects.all()
    restaurants = Restaurant.objects.all()
    agencies = Agency.objects.all()

    return render(request, 'travel/index.html', context={
        "tourPlaces": tourPlaces,
        "hotels": hotels,
        "restaurants": restaurants,
        "agencies": agencies
    })
