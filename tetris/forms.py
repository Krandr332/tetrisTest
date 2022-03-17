import self as self
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import *
from django.contrib.auth.models import User


#
# class LogForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, *kwargs)
#         self.fields['username'].label = 'Логин'
#         self.fields['password'].label = 'Пароль'
#
#     def clean(self):
#         username = self.cleaned_data['username']
#         password = self.cleaned_data['password']
#         if not User.objects.filter(username=username).exists():
#             raise forms.ValidationError(f'тебя {username} нет')
#         user = User.objects.filter(username=username).first()
#         if user:
#             if not user.check_password(password):
#                 raise forms.ValidationError('проебка в пароле')
#         return self.cleaned_data
#
#
# class RegForm(ModelForm):
#     username = forms.CharField(max_length=20, required=True)
#     password = forms.CharField(widget=forms.PasswordInput, required=True)
#     email = forms.EmailInput()
#
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password', 'date_joined']
class LogCheck(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class CreatUserForm(UserCreationForm):
    username = forms.CharField(label='ЛОГИН', widget=forms.TextInput(attrs={'class': 'form-input'}), required=True)
    password1 = forms.CharField(label='ПАРОЛЬ1', widget=forms.PasswordInput(attrs={'class': 'form-input'}),
                                required=True)
    password2 = forms.CharField(label='ПАРОЛЬ2', widget=forms.PasswordInput(attrs={'class': 'form-input'}),
                                required=True)
    email = forms.EmailField(label='ПОЧТА', widget=forms.EmailInput(attrs={'class': 'form-input'}), required=True)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'date_joined']
