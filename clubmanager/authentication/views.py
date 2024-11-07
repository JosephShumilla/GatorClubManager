# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user to the database
            login(request, user)  # Log the user in after sign-up
            return redirect('/myClubs.html')  # Redirect to home page or any other page
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})

def signout_view(request):
    logout(request)
    return redirect(reverse_lazy('login'))