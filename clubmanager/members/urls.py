from django.contrib import admin
from django.urls import path, include
from . import views
from .views import joinClubs

urlpatterns = [
    path('', views.login_user, name="login"),
    path('signUp', views.signup_user, name='signup'),
    path('search/', views.searchClubs, name='search_clubs')
]