from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	return HttpResponse("Meetup webapp")

def login(request):
	return render(request,'login.html')

def createacc(request):
	return render(request,'createacc.html')


def signin(request):
	return render(request,'signin.html')