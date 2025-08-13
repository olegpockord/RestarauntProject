from django.contrib import admin
from django.urls import path

from feedback import views

app_name = 'feedback'

urlpatterns = [
    path('', views.UserContactView.as_view(), name='contact'),
    path('staff/', views.ContactStaffView.as_view(), name='contactStaff'),
]