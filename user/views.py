from django.shortcuts import render


def login(request):
    page = 'login'

    return render(request, 'index.html')


def logout(request):
    return render(request, 'index.html')


def signup(request):
    page = 'signup'

    context = {'page': page}
    return render(request, 'index.html', context)
