from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('login', views.login, name="login"),
	path('createacc', views.createacc, name="createacc"),
	path('signin', views.signin, name="signin"),
]