from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse("<h1>Hello worlds</h1>")


def about(request):
    return HttpResponse("<h1>about blog page</h1>")
