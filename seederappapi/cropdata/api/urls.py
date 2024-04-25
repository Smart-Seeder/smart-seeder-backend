from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('get/', views.get_crops, name='get_crops'),
    # path('get_plate/<int:pk>/', views.get_plate, name='get_plate')
]