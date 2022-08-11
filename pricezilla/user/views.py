from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import RegisterUserForm,LoginForm
from django.contrib.auth import login,authenticate,logout
# Create your views here.

def signup(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user= form.save(commit=False)
            user.username = form.cleaned_data["email"]
            user.set_password(form.cleaned_data["password"])
            user.save()
            login(request,user)
            return redirect(reverse("index"))
    else:
        form = RegisterUserForm()  
    return render(request,"user/sign-up.html",{"form":form})


def loginview(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(username=email,password=password)
            login(request,user)
            print("user logged in")
            return redirect(reverse("index"))
    else:
        form = LoginForm()  
    return render(request,"registration/login.html",{"form":form})

def logoutview(request):
    logout(request)
