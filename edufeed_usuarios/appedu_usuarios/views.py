from django.shortcuts import render
from django.contrib.auth import logout


def home(request):
    return render(request, 'meu_app/home.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            messages.error(request, 'Nome de usuário ou senha incorretos')

    return render(request, 'meu_app/login.html')


def about(request):
    return render(request, 'meu_app/sobre.html')


def user_logout(request):
    logout(request)
    return redirect('home')
