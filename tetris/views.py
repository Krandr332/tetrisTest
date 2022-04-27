import generics as generics
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django import views
from django import template
from django.contrib.auth.forms import UserCreationForm

from .models import Profile
from .forms import CreatUserForm, LogForm
from django.contrib.auth import logout
from .models import Message

from .models import Profile


def home(request):
    """Переодресация"""

    return render(request, 'testT/home.html')


def chat(request):
    """Переодресация"""
    return render(request, 'testT/chat.html')


def game(request):
    """Переодресация"""

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


def index(request):
    return render(request, 'testT/index.html')


def room(request, room_name):
    username = request.GET.get('username', 'Anonymous')
    messages = Message.objects.filter(room=room_name)[0:25]

    return render(request, 'testT/room.html', {'room_name': room_name, 'username': username, 'messages': messages
                                               })
