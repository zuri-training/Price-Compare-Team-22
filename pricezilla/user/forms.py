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
        
        
        
# class SignInForm(forms.Form):
#     """Login form"""
#     email = forms.EmailField(max_length=255,required=True,label="Email")
#     password = forms.CharField(max_length=255,required=True)

class SignInForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True
            
    
    class Meta:
        model = User
        fields = ["email","password"]
        required = ["email","password"]
    
    
