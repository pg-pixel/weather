
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from user_app import views

urlpatterns = [
    path('', views.register , name = 'register'),
]