from django.contrib import admin
from django.urls import path, include
from . import views
from .views import joinClubs

urlpatterns = [
    path('', views.first_view, name='first_view'),
    path('search/', views.searchClubs, name='search_clubs'),
    path('create/',views.createClub, name='create_club'),
]