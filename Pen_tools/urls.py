"""Pen_tools URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from API import views


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', views.index, name="homepage"),
    re_path(r'^contact/$', views.contact, name='contact'),
    re_path(r'^login/$', views.login, name='login'),
    re_path(r'^activerecon/nmap$', views.nmap, name='nmap'),
    re_path(r'^activerecon/hydra$', views.hydra, name='hydra'),
    re_path(r'passiverecon/sherlock$', views.sherlock, name='sherlock'),
    re_path(r'passiverecon/theharvester$', views.theharvester, name='theharvester'),
    re_path(r'enumeration/gobuster$', views.gobuster, name='gobuster'),
    re_path(r'enumeration/nikto$', views.nikto, name='nikto'),
]
