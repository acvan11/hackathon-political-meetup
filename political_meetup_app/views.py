from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProfileForm
from .models import Profile, Venue
from django.views.generic import ListView
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.


def index(request):
    return render(request, 'base.html')


def create_profile(request):
    if request.method == 'POST':
        profile = ProfileForm(request.POST)
        print(profile)
        if profile.is_valid():
            user = profile.save()
            return render(request, 'home.html')
        else:
            print('else')
    else:
        print('create prof - get')
        form = ProfileForm()
        return render(request, 'create_profile.html')


def profile_edit(request, pk):
    profile = User.objects.get(id=pk)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save()
            return redirect('home', pk=artist.pk)
    else:
        form = ProfileForm(instance=profile)
        return render(request, 'profile_form.html', {'form': form})


def default_map(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.eyJ1IjoieWluZWJlYiIsImEiOiJjam13Y3Ixc3MwcjNrM2tydW5lOTh1amxxIn0.YxyWANgIi9iNWOcz6rO_Dg'
    return render(request, 'default.html',
                  {'mapbox_access_token': mapbox_access_token})


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return redirect('index')
    else:
        return render(request, 'login.html', {'error': 'Invalid credentials'})


def signup(request):
    if request.method == 'GET':
        print('GET')
        return render(request, 'signup.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print('POST')
        print(username, password)
        try:
            user = User.objects.create_user(
                username=username,
                password=password)
            print('POST')
            print(username, password)
            if user is not None:
                # auth.login(request, user)
                return redirect('create_profile')
        except Exception as e:
            return render(request, 'signup.html', {'error': 'Arggggg!' + str(e)})
        return HttpResponse('POST to /signup')


def signin(request):
    return render(request, './signin.html')


def profile(request):
    return render(request, './profile.html')


def home(request):
    return render(request, './home.html')
