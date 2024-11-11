from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import sqlite3
from django.http import JsonResponse

from .models import Club, Membership

from django.core.paginator import Paginator


def connnect_database():
    database = sqlite3.connect('db.sqlite3')
    return database

# Function that inserts clubs into the database
def insert_club(database, club_name, club_desc):
    cursor = database.cursor()
    cursor.execute('INSERT INTO Club_Database (club_name, club_desc) VALUES (?, ?)', (club_name, club_desc))
    database.commit()

def item_list(request):
    items = Club.objects.all()  # Fetch all items from the database
    paginator = Paginator(items, 10)  # Show 10 items per page

    page_number = request.GET.get('page')  # Get the page number from the request
    page_obj = paginator.get_page(page_number)  # Get the page of items

    return render(request, 'authenticate/joinClubs.html', {'page_obj': page_obj})

def createClub(request):
    print("create club ran!")
    if request.method == 'POST':
        club_name = request.POST.get('ClubName')
        club_description = request.POST.get('ClubDescription')

        club = Club(club_name=club_name, club_desc=club_description)
        club.save()  # Save the club to the database

        return JsonResponse({'success': True, 'message': 'Club created successfully!'})
    return render(request, 'authenticate/createClub.html',{})
def joinClubs(request):
    clubs = Club.objects.all()
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

def searchClubs(request):
    query = request.GET.get('query', '')
    clubs = Club.objects.filter(club_name__icontains=query)
    paginator = Paginator(clubs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'authenticate/joinClubs.html', {'page_obj': page_obj, 'query': query})
def index(request):
    return render(request, 'authenticate/index.html',{})
def myClubs(request):
    return render(request, 'authenticate/myClubs.html',{})
def upcomingEvents(request):
    return render(request, 'authenticate/upcomingEvents.html',{})
def Sign_In(request):
    return render(request, 'authenticate/login.html',{})