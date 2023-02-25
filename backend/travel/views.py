from django.shortcuts import render, get_object_or_404
from django.conf import settings
from .models import Category, Location, Media, Place
from django.views.generic import ListView, DetailView


# Create your views here.
def index_view(request):
    places = Place.objects.select_related('category', 'location')
    return render(request, 'travel/index.html', {'places': places})


class PlaceListView(ListView):
    model = Place


class PlaceDetailView(DetailView):
    model = Place
