from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import Club, Membership

from django.core.paginator import Paginator



def item_list(request):
    items = Club.objects.all()  # Fetch all items from the database
    paginator = Paginator(items, 10)  # Show 10 items per page

    page_number = request.GET.get('page')  # Get the page number from the request
    page_obj = paginator.get_page(page_number)  # Get the page of items

    return render(request, 'authenticate/joinClubs.html', {'page_obj': page_obj})

def login_user(request):
    return render(request, 'authenticate/Sign_In.html', {})   
def signup_user(request):
    return render(request, 'authenticate/sign_up.html',{})
def createClub(request):
    return render(request, 'authenticate/createClub.html',{})
def joinClubs(request):
    clubs = Club.objects.all()
<<<<<<< HEAD
    return render(request, 'authenticate/joinClubs.html',{'clubs': clubs})
def searchClubs(request):
    query = request.GET.get('query', '')
    if query:
        clubs = Club.objects.filter(club_name__icontains=query)
    else:
        clubs = Club.objects.all()
    return render(request, 'authenticate/joinClubs.html', {'clubs': clubs})
=======
    user = request.user

    ## add membership status to each club
    club_data = []
    for club in clubs:
        if user.is_authenticated:
            is_member = Membership.objects.filter(user=user, club=club).exists()
        else:
            is_member = False
        club_data.append({'club': club, 'is_member': is_member})

    context = {
        'clubs': clubs,
        'club_data': club_data
    }
    return render(request, 'authenticate/joinClubs.html', context=context)
>>>>>>> turillo-authentication
def index(request):
    return render(request, 'authenticate/index.html',{})
def myClubs(request):
    return render(request, 'authenticate/myClubs.html',{})
def upcomingEvents(request):
    return render(request, 'authenticate/upcomingEvents.html',{})
def Sign_In(request):
    return render(request, 'authenticate/Sign_In.html',{})