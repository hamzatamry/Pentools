from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth.models import User
from django.core.files import File
from django.contrib.auth import authenticate, login, logout
from django.db import transaction
from .models import *
from urllib.parse import parse_qs
import datetime
import re
import os
import uuid



variables_dict = {"our_app_name": "PenTools", "tool_used": "nmap"}


class RegistrationView(View):

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


class AuthenticationView(View):

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


class ScanView(View):
    filter = re.compile(r"^(nmap|gobuster|sherlock)[\sa-zA-Z0-9\-./:\\]*$")

    @transaction.atomic
    def get(self, request, *args, **kwargs):

        #   Retrieve query params
        queryparams = request.GET.dict()

        scan_tool = queryparams['scan_tool']
        scan_target = ""
        command = ""

        if scan_tool == 'nmap':
            scan_target = queryparams['scan_target']
            command = "nmap" + " " + queryparams['scan_arguments'] + " " + scan_target
        elif scan_tool == 'gobuster':
            command = "gobuster dir" + " "
            for key, value in queryparams.items():
                if key != "scan_tool":
                    if key == '-u':
                        scan_target = value
                    if key == '-w':
                        switcher = {
                            #   A modifier
                            's': 'C:\\Users\\hamza\\Desktop\\directory-list-2.3-medium.txt',
                            'm': 'C:\\Users\\hamza\\Desktop\\directory-list-2.3-medium.txt',
                            'l': 'C:\\Users\\hamza\\Desktop\\directory-list-2.3-medium.txt'
                        }
                        command += key + " " + switcher.get(value) + " "
                    else:
                        command += key + " " + value + " "
        elif scan_tool == 'sherlock':
            command = "sherlock" + " "

        print(command)

        if request.user.is_authenticated:

            try:

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
                    #   retrieve user
                    user: User = User.objects.get(id=request.user.pk)

                    #   create in target model
                    target: Target = Target.objects.create(target_url=scan_target)

                    #   retrieve pentest_tool
                    pentest_tool: PentestTool = PentestTool.objects.get(pentest_tool_name=scan_tool)

                    scan_start_date = datetime.datetime.now()
                    command_result = os.popen(command).read()
                    scan_end_date = datetime.datetime.now()

                    #   Create a scanresult
                    scan_result = None

                    file_name = f"{uuid.uuid4().hex}" + ".txt"

                    with open(f"uploads/{file_name}", "w") as file_stream:
                        file_stream.write(command_result)

                    with open(f'uploads/{file_name}', 'r+') as file_stream:  # The mode is r+ instead of r
                        scan_result = ScanResult.objects.create(scan_result_file=File(file_stream))

                    #   create a scan
                    scan = Scan.objects.create(scan_start_date=scan_start_date, scan_end_date=scan_end_date, pentest_tool=pentest_tool, user=user, target=target, scan_result=scan_result)

                    return render(request, 'tool.html', context=variables_dict.update(dict({
                        'scan_result': f"{command_result}"
                })))

            except Exception as err:
                print(err)
                return JsonResponse({
                    "message": "Internal Server Error"
                })
        else:
            return render(request, 'login.html', context=variables_dict)


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


