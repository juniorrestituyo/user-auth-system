from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile


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


def logged(request):
    page = 'logged'

    context = {'page': page}
    return render(request, 'index.html', context)


def signup(request):
    page = 'signup'

    context = {'page': page}
    return render(request, 'index.html', context)
