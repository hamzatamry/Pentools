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
    variables_dict["tool_used"] = "nmap.html"
    variables_dict.update({})
    return render(request, 'tool.html', context=variables_dict)


def hydra(request):
    variables_dict["tool_used"] = "hydra.html"
    variables_dict.update({})
    return render(request, 'tool.html', context=variables_dict)


def sherlock(request):
    variables_dict["tool_used"] = "sherlockhtml"
    variables_dict.update({})
    return render(request, 'tool.html', context=variables_dict)


def theharvester(request):
    variables_dict["tool_used"] = "theharvester.html"
    variables_dict.update({})
    return render(request, 'tool.html', context=variables_dict)


def gobuster(request):
    variables_dict["tool_used"] = "gobuster.html"
    variables_dict.update({})
    return render(request, 'tool.html', context=variables_dict)


def nikto(request):
    variables_dict["tool_used"] = "nikto.html"
    variables_dict.update({})
    return render(request, 'tool.html', context=variables_dict)

