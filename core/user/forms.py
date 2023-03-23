from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'short-input'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'short-input'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'long-input'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'long-input'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'long-input'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'long-input'}))
    birthday = forms.DateField(widget=forms.SelectDateWidget(attrs={'class': 'short-input mb-2'}))
    is_employer = forms.BooleanField(required=False, widget=forms.CheckboxInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'birthday', 'is_employer')