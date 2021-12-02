from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View

from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import *
import json


class Registration(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

    def post(self, request: WSGIRequest, *args, **kwargs):

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
        print(request.body)
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

