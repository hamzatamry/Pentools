from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def register(request):
    return HttpResponse("<h1>Registration</h1>")


def authenticate(request):
    return HttpResponse("<h1>Authentication</h1>")
