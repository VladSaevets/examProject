import django.contrib.auth
from django.contrib.auth.models import User
from django.db.models.functions import window
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from project.models import Users


# Create your views here.
def index(request):
    return render(request, 'index.html')

@csrf_exempt
def registration(request):
    if request.method == 'POST':
        nickname = request.POST['nick']
        name = request.POST['name']
        surname = request.POST['surname']
        mail = request.POST['email']
        password = request.POST['password']
        ppassword = request.POST['confPassword']
        users_obj = User.objects.all()
        if password != ppassword:
            return render(request, 'registration/registration.html', {"err": "Пароли не совпадают!"})
        if len(password) < 6:
            return render(request, 'registration/registration.html', {"err": "Пароль слишком короткий!"})
        for i in users_obj:
            if nickname == i.username:
                return render(request, 'registration/registration.html', {"err": "Пользователь с таким ником уже занят!"})
            if mail == i.email:
                return render(request, 'registration/registration.html', {"err": "Данный Email уже занят!"})
        user = User.objects.create_user(nickname, mail, password)
        user.first_name = name
        user.last_name = surname
        user.save()



    return render(request, 'registration/registration.html')

@csrf_exempt
def profile(request):
    return render(request, 'profile.html')

def logout(request):
    if request.user.is_authenticated:
        print('++')
        django.contrib.auth.logout(request)
    return render(request, 'index.html')