from re import search
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    
    path('login/', auth_views.LoginView.as_view(template_name='data/login.html'), name='user-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='data/logout.html'), name='user-logout'),
    path('search/', views.search, name='data-search'),
    path('', views.dataEntry, name='data-entry'),



]

