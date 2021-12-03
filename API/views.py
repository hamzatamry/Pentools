from django.shortcuts import render, redirect
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

    def post(self, request: WSGIRequest, *args, **kwargs):

        try:
            decoded_data = request.body.decode('utf-8')
            parsed_data = parse_qs(decoded_data)

            username = parsed_data['username'][0]
            password = parsed_data['password'][0]
            email = parsed_data['email'][0]
            first_name = parsed_data['first_name'][0]
            last_name = parsed_data['last_name'][0]

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

        return redirect('/', variables_dict.update(dict({
            'id': user.id,
            'username': username,
            'email': email,
            'first_name': first_name,
            'last_name': last_name
        })))


class Authentication(View):

    def post(self, request, *args, **kwargs):
        try:
            decoded_data = request.body.decode('utf-8')
            parsed_data = parse_qs(decoded_data)
            username = parsed_data['username'][0]
            password = parsed_data['password'][0]

            if not username or not password:
                return render(request, 'login.html', context=variables_dict.update(dict({
                    "message": "Users must have a username and password"
                })))

            user = authenticate(username=username, password=password)

            if user is not None:

                login(request, user)
                
                return redirect('/', variables_dict.update(dict({
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

class Scan(View):
    filter = re.compile(r"^(nmap|gobuster|sherlock)[\sa-zA-Z0-9\-./:]*$")

    def get(self, request, *args, **kwargs):

        #   Retrieve query params
        queryparams = request.GET.dict()

        switcher = {
            "nmap": 'nmap',
            "gobuster": 'gobuster dir ',
            "sherlock": 'sherlock',
        }

        command = switcher.get(queryparams['scan_tool'], "")

        for key, value in queryparams.items():
            if key != "scan_tool" and key != "scan_target":
                command += key + " " + value

        command += " " + queryparams['scan_target']

        print(command)

        if request.user.is_authenticated:
            try:

                print(command)
                if not command:
                    return JsonResponse({
                        "message": "no command were specified"
                    })

                #   Filtrer la commande (contre les RCE)
                if not self.filter.fullmatch(command):
                    return JsonResponse({
                        "message": "RCE detected"
                    })
                else:
                    command_result = os.popen(command).read()

                    return HttpResponse(f"{command_result}")

            except Exception as err:
                print(err)
                return JsonResponse({
                    "message": "Internal Server Error"
                })
        else:
            return JsonResponse({
                "message": "Authentication failed"
            })

        return HttpResponse("<h1>here")


class ScanResult(View):
    ScanResult

def index(request):
    variables_dict.update({})
    return render(request, 'index.html', context=variables_dict)


def contact(request):
    variables_dict.update({})
    return render(request, 'contact.html', context=variables_dict)


def login_view(request):
    return render(request, 'login.html', context=variables_dict)


def register(request):
    return render(request, 'register.html', context=variables_dict)


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


