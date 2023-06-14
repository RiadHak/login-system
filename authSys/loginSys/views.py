from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from . forms import CreateUserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def home(request):
    
    return render(request, 'loginSys/home.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')
         
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'loginSys/login.html')
    return render(request, 'loginSys/login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')


def register(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form':form}
    
    return render(request, 'loginSys/register.html', context)