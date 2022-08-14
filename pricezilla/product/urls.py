from django.urls import path
from . import views

urlpatterns = [

    path('category/<slug:slug>', views.category, name='category'),
    path('category/<slug:c_slug>/<slug:p_slug>', views.detail, name='detail')

]