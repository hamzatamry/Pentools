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
from django.urls import path, include, re_path
from API.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('API.urls')),
    re_path(r'^$', index, name='homepage'),
    re_path(r'^register/$', register, name='register'),
    re_path(r'^login/$', login_view, name='login'),
    re_path(r'^logout$', logout_view, name='logout'),
    re_path(r'^contact/$', contact, name='contact'),
    path('<tool_used>/', tool, name='tool')
]
