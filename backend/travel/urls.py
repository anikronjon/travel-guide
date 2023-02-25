from django.urls import path
from . import views


app_name = 'travel'
urlpatterns = [
    path('', views.index_view, name='index'),
    path('place/', views.PlaceListView.as_view(), name='place_list'),
    path('place/<slug:name>/', views.PlaceDetailView.as_view(), name='place_detail'),
]
