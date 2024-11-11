from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', views.signup_view, name='signup'),
    path('signout/', views.signout_view, name='signout'),
]