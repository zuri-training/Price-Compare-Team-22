from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import User
from django import forms

class RegisterUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True
            
    
    class Meta:
        model = User
        fields = ["fullname","email","password"]
        required = ["fullname","email","password"]
    