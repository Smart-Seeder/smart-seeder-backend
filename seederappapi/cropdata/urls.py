from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('api/', include('cropdata.api.urls')),
    path('add/', views.add_crop, name='add_crop'),
    path('get/', views.get_crops, name='get_crops'),
    path('get/<int:pk>/', views.get_crop, name='get_crop'),
]