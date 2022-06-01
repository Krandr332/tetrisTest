import json
from datetime import datetime

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
    score_dict = {}
    user1 = request.user
    o_all = Profile.objects.all()
    q = []
    for i in range(len(o_all)):
        u_all = o_all[i]
        u_all = str(u_all)
        u_all = u_all.split('=')
        score_dict[u_all[0]] = u_all[1]


    print(score_dict)
    contex = {
        'item': score_dict,
    }

    print(contex)
    # return render(request, 'testT/rating.html', contex)
    return render(request, 'testT/rating.html', contex)


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
    if request.POST:
        user1 = request.user
        data = request.body
        data1 = data.decode("utf-8")
        score = (data1.split('&'))[2]
        score = (score.split('='))[1]
        print(score)
        print(user1)
        filter = Profile.objects.filter(user=user1)
        l = len(filter)
        print(l)
        filter_last_score = filter[l - 1]
        print(filter_last_score)
        print(type(filter_last_score))

        filter_last_score = str(filter_last_score)
        filter_last_score = filter_last_score.split('=')
        filter_last_score = filter_last_score[1]
        print(filter_last_score)
        if score > filter_last_score:
            hist = Profile(user=user1, score=score, top_score=score)
            hist.save()

        elif score < filter_last_score:
            hist = Profile(user=user1, score=score, top_score=filter_last_score)
            hist.save()

        print(filter)

        return HttpResponse(data)
    return print(request)
