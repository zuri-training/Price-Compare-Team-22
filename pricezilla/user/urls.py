from django.urls import path

from .views import signup,loginview,logoutview

urlpatterns = [
    path("signup",signup,name="signup"),
    path("login",loginview,name="login"),
    path("logout",logoutview,name="logout")
]