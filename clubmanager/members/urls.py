from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.first_view, name='first_view'),
    path('search/', views.searchClubs, name='search_clubs'),
]