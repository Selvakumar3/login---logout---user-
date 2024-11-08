from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Details
from django.contrib.auth.forms import AuthenticationForm

# new account create

def signup(request):
    if request.method == "POST":
        name  = request.POST['name']
        email = request.POST['email'] 
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 != password2:
            return redirect('signup')
        else:
            obj = User.objects.create_user(username=name,email=email,password=password1)
            obj.save()
            messages.success(request," Registeration Successfully!")
            return redirect('signin')
    else:
        return render(request,"loginup.html")  

# login function

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request,username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "logout successfull")
                return redirect('home')
            else:
                messages.error(request,"login failed!")
                return render('signin')
    form = Details()
    return render(request,'login.html') 
 
# welcome page

def home(request):
    return render(request,'welcome.html')



