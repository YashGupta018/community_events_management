from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserRegistrationForm, EventForm
from .models import Event

# Create your views here.

def register (request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password (password)
            user.save
            login(request, user)
            return redirect('event_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get['username']
        password = request.POST.get['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('event_list')
        else:
            return render(request, 'registration/login.html', {'error': 'Invalid credentials'})
    return render(request, 'registration/login.html')

@login_required
def user_logout(required):
    from django.contrib.auth import logout
    logout(request)
    return redirect('event_list')

@login_required
def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.creator = request.user
            event.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'events/event_form.html', {'form': form, 'action': 'Create'})
    # return render(request, 'registration/event_create.html', {'form': form})