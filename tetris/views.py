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
from .forms import  CreatUserForm, LogCheck


# from tetris.forms import RegForm


def home(request):
    return render(request, 'testT/home.html')


def auth(request):
    return render(request, 'testT/register.html')



def reg(request):
    form = UserCreationForm
    context = {'form': form}
    form = UserCreationForm()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return render(request, 'testT/register.html', {'form': form})
    return render(request, 'testT/register.html', context)

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
