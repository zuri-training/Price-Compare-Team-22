from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model



class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model= get_user_model()
        fields = ['username', 'password1', 'password2']


    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args,  **kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-control', 'style':'padding:10px;', 'placeholder':'debbie'})
        self.fields['password1'].widget.attrs.update({'class':'form-control', 'placeholder':'Enter password ...'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm password...'})

# class RegisterUserForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         for field in self.Meta.required:
#             self.fields[field].required = True
            
    
#     class Meta:
#         model = User
#         fields = ["fullname","email","password"]
#         required = ["fullname","email","password"]
        
        
        
# class SignInForm(forms.Form):
#     """Login form"""
#     email = forms.EmailField(max_length=255,required=True,label="Email")
#     password = forms.CharField(max_length=255,required=True)

# class SignInForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         for field in self.Meta.required:
#             self.fields[field].required = True
            
    
#     class Meta:
#         model = User
#         fields = ["email","password"]
#         required = ["email","password"]
    
    
