from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import User
from django import forms

class RegisterUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ["fullname","username","email","password1","password2"]
    