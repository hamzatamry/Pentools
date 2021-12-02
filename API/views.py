from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

variables_dict = {"our_app_name": "PenTools", "tool_used": "nmap"}


def index(request):
    variables_dict.update({})
    return render(request, 'index.html', context=variables_dict)


def contact(request):
    variables_dict.update({})
    return render(request, 'contact.html', context=variables_dict)


def login(request):
    variables_dict.update({})
    return render(request, 'login.html', context=variables_dict)


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

