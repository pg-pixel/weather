from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout

from django import forms 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 

class CustomRegisterForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15)
    email = forms.EmailField()
    
    class Meta:
        model = User 
        fields = ['email', 'username', 'phone_number', 'password1', 'password2']
        
