from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime


class User(AbstractUser):
    birthday = models.DateField(default=datetime.date.today)
    is_employer = models.BooleanField(default=False)


class Resume(models.Model):
    name = models.CharField(max_length=100)
    experience = models.IntegerField(blank=True, default=0)
    exp_description = models.TextField(blank=True)
    skills = models.TextField()
    languages = models.TextField()
    description = models.TextField()
    contacts = models.TextField()


class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    main_office_city = models.CharField(max_length=100)
    main_office_address = models.CharField(max_length=200)
    work_since = models.DateField()
    contacts = models.TextField()

