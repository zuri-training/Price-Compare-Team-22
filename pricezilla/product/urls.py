from django.urls import path
from . import views

urlpatterns = [
    path('furnitures/', views.furniture, name='furnitures')
]