"""
URL configuration for clubmanager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from members import views


urlpatterns = [
    path('', views.first_view, name='first_view'),
    path('admin/', admin.site.urls),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    path('createClub.html', views.createClub, name='createClub'),
    path('joinClubs.html', views.item_list, name='joinClub'),
    path('myClubs.html', views.myClubs, name='myClubs'),
    path('upcomingEvents.html', views.myClubEvents, name='upcomingEvents'),
    path('join/', views.joinSpecificClub, name='join_specific_club'),
    path('leave/', views.leaveSpecificClub, name='leave_specific_club'),
    path('createEvent/<int:club_id>/', views.createEvent, name='create_event'),
    path('searchEvents/', views.searchEvents, name='search_events'),
]
## user login/logout authentication

urlpatterns += [
    path('accounts/', include('authentication.urls')),
]
