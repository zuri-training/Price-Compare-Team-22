from site import abs_paths
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    fullname = models.CharField(max_length=200,blank=True)    
    
    def __str__(self):
        return f"{self.username}"
    
    def get_full_name(self) -> str:
        return self.fullname
    
    