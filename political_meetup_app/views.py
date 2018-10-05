from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	return HttpResponse("Meetup webapp")

def login(request):
	return render(request,'./political_meetup_app/login.html')

def signup(request):
	return render(request,'./signup.html')

def signin(request):
	return render(request,'./signin.html')

def profile(request):
	return render(request,'./profile.html')

def home(request):
	return render(request,'./home.html')