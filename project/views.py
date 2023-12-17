from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
    return render(request, 'index.html')

@csrf_exempt
def registration(request):
    return render(request, 'registration.html')

@csrf_exempt
def authorization(request):
    return render(request, 'authorization.html')


def cabinet(request):
    return render(request, 'cabinet.html')