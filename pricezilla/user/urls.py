from django.urls import path

from .views import signup,loginview,logout

urlpatterns = [
    path("signup",signup,name="signup"),
    path("login",loginview,name="login"),
    path("logout",logout,name="logout")
]
