from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import Club, Membership

from django.core.paginator import Paginator


def first_view(request):
    if request.user.is_authenticated:
        print('User is authenticated')
        return redirect('home')
    else:
        print('User is not authenticated')
        return redirect('login')

def item_list(request):
    items = Club.objects.all()  # Fetch all items from the database
    paginator = Paginator(items, 10)  # Show 10 items per page

    page_number = request.GET.get('page')  # Get the page number from the request
    page_obj = paginator.get_page(page_number)  # Get the page of items

    return render(request, 'main_sites/joinClubs.html', {'page_obj': page_obj})

def createClub(request):
    return render(request, 'main_sites/createClub.html',{})

def joinSpecificClub(request):
    club_id = request.POST.get('club_id')
    club = Club.objects.get(id=club_id)
    user = request.user
    print(user, club)
    if user.is_authenticated:
        is_member = Membership.objects.filter(user=user, club=club).exists()
        if not is_member:
            membership = Membership(user=user, club=club, role='Member')
            membership.save()
            messages.success(request, f'You have joined {club.club_name}')
        else:
            messages.error(request, f'You are already a member of {club.club_name}')
    else:
        messages.error(request, 'You must be logged in to join a club')
    return redirect('home')

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
    return render(request, 'main_sites/joinClubs.html', context=context)

def searchClubs(request):
    query = request.GET.get('query', '')
    clubs = Club.objects.filter(club_name__icontains=query)
    paginator = Paginator(clubs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'main_sites/joinClubs.html', {'page_obj': page_obj, 'query': query})
def index(request):
    return render(request, 'main_sites/index.html',{})
def myClubs(request):
    return render(request, 'main_sites/myClubs.html',{})
def upcomingEvents(request):
    return render(request, 'main_sites/upcomingEvents.html',{})