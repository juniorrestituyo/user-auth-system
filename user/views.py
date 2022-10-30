from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile


def login(request):
    page = 'login'

    return render(request, 'index.html')


def logout(request):
    return render(request, 'index.html')


def loged(request):
    page = 'loged'

    context = {'page': page}
    return render(request, 'index.html', context)


def signup(request):
    page = 'signup'

    context = {'page': page}
    return render(request, 'index.html', context)
