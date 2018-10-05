from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProfileForm
from .models import User, Venue
from django.views.generic import ListView
from django.conf import settings


# Create your views here.


def index(request):
    return render(request, 'base.html')


def create_profile(request):
    if request.method == 'POST':
        profile = ProfileForm(request.POST)
        print(profile)
        if profile.is_valid():
            user = profile.save()
            return render(request, 'base.html')
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


class VenueAdmin(ListView):
    model = Venue
    list_display = ('name', 'latitude', 'longitude',)
    search_fields = ('name',)

    fieldsets = (
        (None, {
            'fields': ('name', 'latitude', 'longitude',)
        }),
    )

    class Media:
        if hasattr(settings, 'GOOGLE_MAPS_API_KEY') and settings.GOOGLE_MAPS_API_KEY:
            css = {
                'all': ('location_picker.css',),
            }
            js = (
                'https://maps.googleapis.com/maps/api/js?key={}'.format(
                    settings.GOOGLE_MAPS_API_KEY),
                'location_picker.js',
            )


def login(request):
    return render(request, './political_meetup_app/login.html')


def signup(request):
    return render(request, './signup.html')


def signin(request):
    return render(request, './signin.html')


def profile(request):
    return render(request, './profile.html')


def home(request):
    return render(request, './home.html')
