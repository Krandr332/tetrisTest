import json

import generics as generics
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.sites import requests
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseServerError
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django import views
from django import template
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from .forms import CreatUserForm, LogForm, GameHistoryForm
from django.contrib.auth import logout

from .models import Profile


def home(request):
    """Переодресация"""

    return render(request, 'testT/home.html')


def chat(request):
    """Переодресация"""
    return render(request, 'testT/chat.html')


def game(request):
    return render(request, 'testT/game.html')


def auth(request):
    """Переодресация"""

    return render(request, 'testT/auth.html')


def history(request):
    """Фильтрация значений бд для вывода значений историй игр"""

    contex = {
        'items': Profile.objects.filter(user=request.user.id)
    }
    return render(request, 'testT/history.html', contex)


def rating(request):
    """Фильтрация значений бд для вывода значений рейтинга"""

    contex = {
        'items': Profile.objects.all(),
    }

    return render(request, 'testT/history.html', contex)


def reg(request):
    """Регистрация юзера"""

    form_u = UserCreationForm(request.POST)
    new_user = None
    if request.method == 'POST':
        if form_u.is_valid():
            new_user = form_u.save(commit=False)
            new_user.set_password(form_u.cleaned_data['password2'])
            new_user.save()
            # Profile.objects.create(**{'user': new_user})

        else:
            print(form_u.errors)

        return render(request, 'testT/register.html', {'new_user': new_user})
    return render(request, 'testT/register.html', {'form_u': form_u})


def avtoriz(request):
    """авторизация юзера"""

    form = LogForm(request.POST)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            redirect('/tetris/')
        else:
            print(form.errors)
    return render(request, 'testT/auth.html', {'form': form})


def exit(request):
    """выход юзера из ака"""
    logout(request)
    return render(request, 'testT/home.html')


def help_me_please(request):
    form = GameHistoryForm(request.POST)
    if request.POST:
        user1 = request.user.id
        data = request.body
        data1 = data.decode("utf-8")
        score = (data1.split('&'))[2]
        score = (score.split('='))[1]
        print(score)
        print(user1)
        s = Profile(score,user1)
        print(s)

        return HttpResponse(data)
    return print(request)
