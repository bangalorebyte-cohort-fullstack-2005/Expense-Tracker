from django import forms
from django.contrib.auth.forms import UserCreationForm
from expense_tracker.models import *

class RegistarationForm(UserCreationForm):
    email= forms.EmailField(max_length= 75, help_text= Email Address Required)

    class Meta:
        model= Account