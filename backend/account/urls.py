from django.urls import path, include
from . import views


app_name = 'account'
urlpatterns = [
    path('signin/', views.signin_view, name='signin'),
    path('signup/', views.signup_view, name='signup')
]
