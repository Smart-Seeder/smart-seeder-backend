from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('add/', views.add_crop, name='add_crop'),
    path('get/', views.get_crops, name='get_crops'),
    path('get/<int:pk>/', views.get_crop, name='get_crop'),
    path('get_plate/<int:pk>/', views.get_plate, name='get_plate'),
    path('fetch_realtime_data/', views.fetch_realtime_data, name='fetch_realtime_data'),
]