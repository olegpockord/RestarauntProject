from django.contrib import admin
from django.urls import path

from user import views


app_name = 'users'

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('logout/', views.logout, name='logout'),
]