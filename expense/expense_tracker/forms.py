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