from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import RegisterUserForm
from django.contrib.auth import login

# Create your views here.

def signup(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user= form.save()
            login(request,user)
            return redirect(reverse("login"))
    else:
        form = RegisterUserForm()  
    return render(request,"registration/sign-up.html",{"form":form})
