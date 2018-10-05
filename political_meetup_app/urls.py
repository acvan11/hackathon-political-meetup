from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('profile/', views.profile, name='profile'),
    path('create_profile', views.profile, name='create_profile'),
    path('home/', views.home, name='home'),
    path('map', views.VenueAdmin.as_view(), name='map')
]
