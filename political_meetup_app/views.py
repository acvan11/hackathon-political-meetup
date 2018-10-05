from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProfileForm
from .models import User
# Create your views here.


def index(request):
    return render(request, 'base.html')


def profile(request):
    if request.method == 'POST':
        profile = ProfileForm(request.POST)
        if profile.is_valid():
            user = profile.save()
            return redirect('base.html')
    else:
        form = ProfileForm()
        return render(request, 'profile.html')


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
