from django.contrib.sessions.models import Session
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View

from django.contrib.auth import authenticate, login
from .models import *
import json
import re
import os


class Registration(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

    def post(self, request, *args, **kwargs):

        data = json.loads(request.body)

        try:
            username = data['username']
            password = data['password']
            email = data['email']
            first_name = data['first_name']
            last_name = data['last_name']

            if not username or not password or not email or not first_name or not last_name:
                return JsonResponse({
                    "message": "Users must have a username, a password, an email, ..."
                })

            user = User.objects.create_user(username=username, password=password)
            user.email = email
            user.first_name = first_name
            user.last_name = last_name
            user.save()
        except Exception as err:
            print(err)
            return JsonResponse({
                "message": "Internal server error"
            })

        return JsonResponse({
            'id': user.id,
            'username': username,
            'email': email,
            'first_name': first_name,
            'last_name': last_name
        })

class Authentication(View):

    def post(self, request, *args, **kwargs):

        data = json.loads(request.body)

        try:
            username = data['username']
            password = data['password']

            if not username or not password:
                return JsonResponse({
                    "message": "Users must have a username and password"
                })

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return JsonResponse({
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'first_name': user.first_name,
                    'last_name': user.last_name
                })
            else:
                return JsonResponse({
                    "message": "Authentication needed"
                })
        except Exception as err:
            print(err)
            return JsonResponse({
                "message": "Internal Server Error"
            })


class Scan(View):

    filter = re.compile(r"^(nmap|gobuster|sherlock)[\sa-zA-Z0-9-./:]*$")

    def post(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            try:
                data = json.loads(request.body)
                command = data['command']

                if not command:
                    return JsonResponse({
                        "message": "no command were specified"
                    })

                #   Filtrer la commande
                if not self.filter.fullmatch(command):
                    return JsonResponse({
                        "message": "RCE detected"
                    })
                else:
                    command_result = os.popen(command).read()
                    return HttpResponse(f"{command_result}")

            except Exception as err:

                return JsonResponse({
                    "message": "Internal Server Error"
                })
        else:
            return JsonResponse({
                "message": "Authentication needed"
            })