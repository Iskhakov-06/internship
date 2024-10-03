from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def view_1(request):
    return HttpResponse('first page from app "test_1"')


def view_2(request):
    return HttpResponse('second page from app "test_1"')


def view_3(request):
    return HttpResponse('third page from app "test_1"')

