from django.db import models
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import MeetLink

class RegisterUserForm(UserCreationForm):
    GENDER = (('Male', 'Male'),('Female', 'Female'),('Other', 'Other'))
    gender = forms.ChoiceField(choices=GENDER)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1',
                  'password2', 'gender']

class UpdateMeeting(ModelForm):
    class Meta:
        model = MeetLink
        fields = '__all__'
        exclude = ['user']