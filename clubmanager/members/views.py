from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Club

def login_user(request):
    return render(request, 'authenticate/Sign_In.html', {})   
def signup_user(request):
    return render(request, 'authenticate/sign_up.html',{})
def createClub(request):
    return render(request, 'authenticate/createClub.html',{})
def joinClubs(request):
    clubs = Club.objects.all()
    return render(request, 'authenticate/joinClubs.html',{'clubs': clubs})
def searchClubs(request):
    query = request.GET.get('query', '')
    if query:
        clubs = Club.objects.filter(club_name__icontains=query)
    else:
        clubs = Club.objects.all()
    return render(request, 'authenticate/joinClubs.html', {'clubs': clubs})
def index(request):
    return render(request, 'authenticate/index.html',{})
def myClubs(request):
    return render(request, 'authenticate/myClubs.html',{})
def upcomingEvents(request):
    return render(request, 'authenticate/upcomingEvents.html',{})
def Sign_In(request):
    return render(request, 'authenticate/Sign_In.html',{})