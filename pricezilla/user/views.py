from django.shortcuts import render,redirect
from django.urls import reverse
# from .forms import RegisterUserForm,SignInForm
from django.contrib.auth import login,authenticate,logout
from .forms import CustomUserCreationForm
# Create your views here.
def signup(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            user = authenticate(request, username = user.username, password = request.POST['password1'])

            if user is not None:
                login(request, user)
                return redirect('index')
    context={'form': form}
    return render(request, 'registration/sign-up.html',context)
# def signup(request):
#     if request.method == "POST":
#         form = RegisterUserForm(request.POST)
#         if form.is_valid():
#             user= form.save(commit=False)
#             user.username = form.cleaned_data["email"]
#             user.set_password(form.cleaned_data["password"])
#             user.save()
#             login(request,user)
#             return redirect(reverse("index"))
#     else:
#         form = RegisterUserForm()  
#     return render(request,"registration/sign-up.html",{"form":form})

def loginview(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']


        user = authenticate(request, username=username, password=password)
        print('USER:', user)
        if user is not None:
            login(request, user)
            return redirect('index')
    return render(request, 'registration/login.html')

def logoutview(request):
    logout(request)
    return redirect('login')

# def loginview(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password=request.POST['password']
#         if user is not None:
#             login(request, user)
#             return redirect('index')
#         user = authenticate(request, username=email, password = password)
#         print("USER:", user)
#         form = SignInForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data["email"]
#             password = form.cleaned_data["password"]
#             # user = authenticate(username=email,password=password)
#             login(request,user)
#             print("user logged in")
#             return redirect(reverse("index"))
#     else:
#         form = SignInForm()
#     return render(request,"registration/login.html",{"form":form})

# def logoutview(request):
#     logout(request)
#     return redirect(reverse("index"))
   
