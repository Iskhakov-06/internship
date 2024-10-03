from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def view_1(request):
    return HttpResponse('Первая страница из приложения "test_1"')


def view_2(request):
    return HttpResponse('Вторая страница из приложения "test_1"')


def view_3(request):
    return HttpResponse('Третья страница из приложения "test_1"')

