from django.contrib.auth import authenticate, login
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

from .models import Profile


def home(request):
    return render(request, 'testT/home.html')


def game(request):
    return render(request, 'testT/game.html')


def auth(request):
    return render(request, 'testT/auth.html')


def history(request):
    item = Profile.objects.filter(author=request.user)
    return render(request, 'testT/history.html',{'item': item})


def reg(request):
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
    logout(request)
    return render(request, 'testT/home.html')
