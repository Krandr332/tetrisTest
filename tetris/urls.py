from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('auth/', avtoriz, name='auth'),
    path('register/', reg, name='reg'),
    path('exit/', exit, name='exit'),
    path('game/', game, name='game'),
    path('history/', history, name='history'),
    path('rating/', rating, name='rating'),
    path('chat/', chat, name='chat'),

]
# Функции views:
#     def home(request): - Переодресация
#     def chat(request): - Переодресация
#     def game(request): - Переодресация
#     def auth(request): - Переодресация
#     def history(request): - Филь-я знач-й бд для вывода знач-й истории
#     def rating(request): - Филь-я знач-й бд для вывода знач-й рейтинга
#     def reg(request):  - Регистрация юзера
#     def avtoriz(request): - Авторизация юзера
#     def exit(request): - Выход юзера из ака