from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *
from urllib.parse import parse_qs
import json
import re
import os


variables_dict = {"our_app_name": "PenTools", "tool_used": "nmap"}


class Registration(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'register.html', context=variables_dict)

    def post(self, request: WSGIRequest, *args, **kwargs):

        data = parse_qs(request.body.decode("utf-8"))
        data = {x: y[0] for (x, y) in data.items()}
        # data = json.loads(request.body)

        try:
            username = data['username']
            password = data['password']
            email = data['email']
            first_name = data['first_name']
            last_name = data['last_name']

            if not username or not password or not email or not first_name or not last_name:
                return render(request, 'register.html', context=variables_dict.update(dict({
                    "message": "Users must have a username, a password, an email, ..."
                })))

            user = User.objects.create_user(username=username, password=password)
            user.email = email
            user.first_name = first_name
            user.last_name = last_name
            user.save()
        except Exception as err:
            print(err)
            return render(request, 'register.html', context=variables_dict.update(dict({
                "message": "Internal server error"
            })))

        return render(request, 'index.html', context=variables_dict.update(dict({
            'id': user.id,
            'username': username,
            'email': email,
            'first_name': first_name,
            'last_name': last_name
        })))


class Authentication(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'login.html', context=variables_dict)

    def post(self, request, *args, **kwargs):
        try:
            data = parse_qs(request.body.decode("utf-8"))
            data = {x: y[0] for (x, y) in data.items()}
            print(data)

            username = data['username']
            password = data['password']

            print(username)
            print(password)

            if not username or not password:
                return render(request, 'login.html', context=variables_dict.update(dict({
                    "message": "Users must have a username and password"
                })))

            user = authenticate(username=username, password=password)

            if user is not None:

                login(request, user)

                return render(request, 'index.html', context=variables_dict.update(dict({
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'first_name': user.first_name,
                    'last_name': user.last_name
                })))
            else:
                return render(request, 'login.html', context=variables_dict.update(dict({
                    "message": "Authentication failed"
                })))
        except Exception as err:
            print(err)
            return render(request, 'login.html', context=variables_dict.update(dict({
                "message": "Internal Server Error"
            })))

def logout_view(request):
    logout(request)
    return render(request, 'login.html', context=variables_dict)


def index(request):
    variables_dict.update({})
    return render(request, 'index.html', context=variables_dict)


def contact(request):
    variables_dict.update({})
    return render(request, 'contact.html', context=variables_dict)


''' def login(request):
    variables_dict.update({})
    return render(request, 'login.html', context=variables_dict)


def register(request):
    variables_dict.update({})
    return render(request, 'register.html', context=variables_dict) '''


def nmap(request):
    variables_dict["tool_used"] = "nmap"
    variables_dict.update({})
    return render(request, 'tool.html', context=variables_dict)


def hydra(request):
    variables_dict["tool_used"] = "hydra"
    variables_dict.update({})
    return render(request, 'tool.html', context=variables_dict)


def sherlock(request):
    variables_dict["tool_used"] = "sherlock"
    variables_dict.update({})
    return render(request, 'tool.html', context=variables_dict)


def theharvester(request):
    variables_dict["tool_used"] = "theharvester"
    variables_dict.update({})
    return render(request, 'tool.html', context=variables_dict)


def gobuster(request):
    variables_dict["tool_used"] = "gobuster"
    variables_dict.update({})
    return render(request, 'tool.html', context=variables_dict)


def nikto(request):
    variables_dict["tool_used"] = "nikto"
    variables_dict.update({})
    return render(request, 'tool.html', context=variables_dict)

