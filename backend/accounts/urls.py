from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('signin/', views.signin_view, name='signin'),
    path('signup/', views.signup_view, name='signup'),
    path('profile/', views.profile_view, name='profile'),
]
