from django.contrib import admin
from django.urls import path, include
from . import views as bus_views

urlpatterns = [
    path('map', bus_views.map_bus),

]
