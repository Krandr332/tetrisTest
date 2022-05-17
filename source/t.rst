Вьюхи
------

.. automodule:: views
    :members:




.. note::
    Проект находится в стадии разработки

.. code-block:: python


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

           return render(request, 'testT/register.html',
            {'new_user': new_user})
       return render(request, 'testT/register.html',
        {'form_u': form_u})




   def avtoriz(request):
       """авторизация юзера"""

       form = LogForm(request.POST)
       if request.method == 'POST':
           username = request.POST.get('username')
           password = request.POST.get('password')
           user = authenticate(request, username=username,
            password=password)
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


