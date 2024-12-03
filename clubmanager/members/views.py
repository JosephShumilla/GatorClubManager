from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import Club, Membership, Event
from .forms import EventForm

from django.core.paginator import Paginator

def myClubEvents(request):
    user = request.user
    if user.is_authenticated:
        # Get all clubs the user is a member of
        memberships = Membership.objects.filter(user=user)
        clubs = [membership.club for membership in memberships]

        # Fetch all events for these clubs
        events = Event.objects.filter(club__in=clubs).order_by('start_time')
    else:
        context = {
            'message': 'You must be logged in to see events'
        }
        return render(request, 'main_sites/not_authenticated.html', context)

    # Paginate the events
    paginator = Paginator(events, 10)  # Show 10 events per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Prepare event data for the template
    event_data = []
    for event in page_obj:
        event_data.append({
            'event': event,
            'club': event.club
        })

    context = {
        'page_obj': page_obj,
        'event_data': event_data,
    }

    return render(request, 'main_sites/upcomingEvents.html', context=context)

def first_view(request):
    if request.user.is_authenticated:
        print('User is authenticated')
        return redirect('myClubs')
    else:
        print('User is not authenticated')
        return redirect('login')

def item_list(request):
    items = Club.objects.all()  # Fetch all items from the database
    paginator = Paginator(items, 10)  # Show 10 items per page

    page_number = request.GET.get('page')  # Get the page number from the request
    page_obj = paginator.get_page(page_number)  # Get the page of items

    user = request.user
    club_data = []
    for item in page_obj.object_list:
        if user.is_authenticated:
            is_member = Membership.objects.filter(user=user, club=item).exists()
        else:
            is_member = False
        club_data.append({'club': item, 'is_member': is_member})
    
    context = {
        'page_obj': page_obj,
        'club_data': club_data
    }

    return render(request, 'main_sites/joinClubs.html', context=context)

def createClub(request):
    user = request.user
    if not user.is_authenticated:
        context = {
            'message': 'You must be logged in to create a club'
        }
        return render(request, 'main_sites/not_authenticated.html', context)
    
    if request.method == 'POST':
        club_name = request.POST.get('ClubName')
        club_description = request.POST.get('ClubDescription')
        instagram = request.POST.get('Socials')
        discord = request.POST.get('Socials')
        twitter = request.POST.get('Socials')
        # Create and save a new club instance
        new_club = Club(
            club_name=club_name,
            club_desc=club_description,
        )
        new_club.save()

        # add the user as the manager of the club
        membership = Membership(user=user, club=new_club, role='Manager')
        membership.save()

    return render(request, 'main_sites/createClub.html',{})

def createEvent(request, club_id):
    print("ran")
    club = get_object_or_404(Club, id=club_id)  # Fetch the club based on the passed club_id
    user = request.user
    if not user.is_authenticated:
        context = {
            'message': 'You must be logged in to create an event'
        }
        return render(request, 'main_sites/not_authenticated.html', context)
    if not Membership.objects.filter(user=user, club=club, role='Manager').exists():
        context = {
            'message': 'You must be a manager of the club to create an event'
        }
        return render(request, 'main_sites/not_authenticated.html', context)

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)  # Don't save the event yet
            event.club = club  # Associate the event with the club
            event.save()  # Now save the event
            return redirect('upcomingEvents')
    else:
        form = EventForm()

    return render(request, 'main_sites/createEvent.html', {'form': form, 'club': club})


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
    return redirect('myClubs')

def leaveSpecificClub(request):
    club_id = request.POST.get('club_id')
    club = Club.objects.get(id=club_id)
    user = request.user
    print(user, club)
    
    if user.is_authenticated:
        try:
            membership = Membership.objects.get(user=user, club=club)
            membership.delete()
            messages.success(request, f'You have left {club.club_name}')
        except Membership.DoesNotExist:
            messages.error(request, f'You are not a member of {club.club_name}')
    else:
        messages.error(request, 'You must be logged in to leave a club')
    
    return redirect('myClubs')

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

    user = request.user
    club_data = []
    for item in page_obj.object_list:
        if user.is_authenticated:
            is_member = Membership.objects.filter(user=user, club=item).exists()
        else:
            is_member = False
        club_data.append({'club': item, 'is_member': is_member})
    
    context = {
        'page_obj': page_obj,
        'club_data': club_data
    }

    return render(request, 'main_sites/joinClubs.html', context=context)

def myClubs(request):
    user = request.user
    if user.is_authenticated:
        memberships = Membership.objects.filter(user=user)
        clubs = [membership.club for membership in memberships]
    else:
        context = {
            'message': 'You must be logged in to view your clubs'
        }
        return render(request, 'main_sites/not_authenticated.html', context)

    paginator = Paginator(clubs, 10)  # Show 10 clubs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    club_data = []
    for item in page_obj.object_list:
        if user.is_authenticated:
            is_member = Membership.objects.filter(user=user, club=item).exists()
            is_manager = Membership.objects.filter(user=user, club=item, role='Manager').exists()
        else:
            is_member = False
            is_manager = False
        club_data.append({'club': item, 'is_member': is_member, 'is_manager': is_manager})

    context = {
        'page_obj': page_obj,
        'club_data': club_data
    }

    return render(request, 'main_sites/myClubs.html', context=context)

def index(request):
    return render(request, 'main_sites/index.html',{})
def upcomingEvents(request):
    return render(request, 'main_sites/upcomingEvents.html',{})