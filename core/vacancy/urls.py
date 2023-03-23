from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'vacancy'
urlpatterns = [
    path('', main, name='main'),
    path('vacancies/', vacancies, name='vacancies'),
]