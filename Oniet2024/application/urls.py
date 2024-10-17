from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views
from .views import obtain_data



urlpatterns = [
    path('', obtain_data, name='home')
]