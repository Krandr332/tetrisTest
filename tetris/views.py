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
from .forms import CreatUserForm, LogCheck


# from tetris.forms import RegForm


def home(request):
    return render(request, 'testT/home.html')


def auth(request):
    return render(request, 'testT/register.html')


def reg(request):
    form_u = UserCreationForm(request.POST)
    new_user = None
    if request.method == 'POST':
        if form_u.is_valid():
            new_user = form_u.save(commit=False)
            new_user.set_password(form_u.cleaned_data['password2'])
            new_user.save()
        else:
            print(form_u.errors)

        return render(request, 'testT/register.html', {'new_user': new_user})
    return render(request, 'testT/register.html', {'form_u': form_u})


# def reg(request):
#     form = RegForm()
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#     return render(request, 'testT/register.html', {'form': form})


def avtoriz(request):
    form = LogCheck()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            login(request, username)
            redirect('home')
    return render(request, 'testT/auth.html', {'form': form})
