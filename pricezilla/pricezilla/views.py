from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request,"about.html")

def login(request):
    return render(request, "login.html")

def contact(request):
    return render(request, "contact.html")

def account(request):
    return render(request, "account-info.html")

def sign(request):
    return render(request, "sign-up.html")

def profile(request):
    return render(request, "profile.html")

