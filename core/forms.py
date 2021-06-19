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

    # def clean_username(self):
    #     username = self.cleaned_data.get('username')
    #     qs = User.objects.filter(username__iexact=username)
    #     if not qs.exists():
    #         raise forms.ValidationError('This username is already taken.')
    #     return username
    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     qs = User.objects.filter(email__iexact=email)
    #     if not qs.exists():
    #         raise forms.ValidationError('This email is already taken.')
    #     return email

class UpdateMeeting(ModelForm):
    class Meta:
        model = MeetLink
        fields = '__all__'
        exclude = ['user']