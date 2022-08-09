from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import RegisterUserForm
from django.contrib.auth import login

# Create your views here.

def signup(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user= form.save(commit=False)
            user.username = form.cleaned_data["email"]
            user.set_password(form.cleaned_data["password"])
            user.save()
            print(user)
            login(request,user)
            return redirect(reverse("index"))
    else:
        form = RegisterUserForm()  
    return render(request,"user/sign-up.html",{"form":form})
