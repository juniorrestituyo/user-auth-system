from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import is_valid_path

from .models import Profile
from .forms import CustomUserCreationForm


def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('logged')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('logged')
        else:
            messages.error(request, 'Username or password is incorrect')

    return render(request, 'index.html')


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def logged(request):
    return render(request, 'logged.html')


def signup(request):
    page = 'signup'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, "User account was created")

            login(request, user)
            return redirect('login')
        
        else:
            messages.error(request, "An error has occurred during registration")

    context = {'page': page, 'form': form}
    return render(request, 'index.html', context)
