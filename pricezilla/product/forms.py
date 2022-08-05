from django.forms import ModelForm


from .models import Order
from django.contrib.auth import get_user_model



class OrderForm(ModelForm):
    
    class Meta:
        model = Order
        fields = '__all__'
        
        widgets = {
            
        }