from django.urls import path
from . import views

urlpatterns = [

    path('furnitures/', views.furniture, name='furniture'),
    path('entertainement/', views.entertainement, name='entertainement'),
    path('kitchen/', views.kitchen, name='kitchen'),
    path('laundry/', views.laundry, name='laundry'),

]