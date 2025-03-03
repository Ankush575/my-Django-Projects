from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistratinForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

# function to get user registered


def registerUser(request):
    if request.method == 'POST':
        form = RegistratinForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('tasklist')
    else:
        form = RegistratinForm()
    return render(request, 'register.html', {'form': form})

# function to get user logged in


def loginUser(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('tasklist')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# function to get user logged out


def logoutUser(request):
    logout(request)
    return redirect('login')
