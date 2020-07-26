from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def result(request):
    age = request.GET['user_age']
    return render(request, 'result.html', {'age': age})
