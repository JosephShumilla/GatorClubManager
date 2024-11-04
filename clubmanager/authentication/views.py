# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy

def signup_view(request):
    request.session['logged_in']
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user to the database
            login(request, user)  # Log the user in after sign-up
            return redirect('')  # Redirect to home page or any other page
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})