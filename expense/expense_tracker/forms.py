from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from expense_tracker.models import *

#using built-in form
class RegistrationForm(UserCreationForm):
    email= forms.EmailField(max_length= 75, help_text= Email Address Required)

    class Meta:
        model= Account
        fields= ('email', 'username', 'password1', 'password2')

#creating a custom form
class AuthenticationForm(forms.ModelForm):
    password= form.CharField(label= 'Password', widget= forms.PasswordInput)

    class Meta:
        model= Account
        field= ('email', 'password')

    def clean(self):
        if self.is_valid():
            email= self.cleaned_data['email']
            password= self.cleaned_data['password']
            if not authenticate(email= email, password= password):
                raise forms.ValidationError("Invalid credentials")

#updating account form
class UpdateForm(form.ModelForm):

    class Meta:
        model= Account
        fields= ("email", "username")
    def clean_email(self):
        if self.is_valid():
            email= self.cleaned_data['email']
            try:
                account= Account.objects.exclude(pk= self.instance.pk).get(email= email)
            except Account.DoesNotExist:
                return email
            raise forms.ValidationError('Email "%s" is already in use'% account.email)
    
    def clean_username(self):
        if self.is_valid():
            username= self.cleaned_data['username']
            try:
                account= Account.objects.exclude(pk= self.instance.pk).get(username= username)
            except Account.DoesNotExist:
                return username
            raise forms.ValidationError('Username "%s" is already in use'% account.username)
