from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'user'
urlpatterns = [
    path('sign-up/', sign_up, name='sign-up'),
]