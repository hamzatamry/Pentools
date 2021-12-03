from django.urls import path, re_path
from .views import *
from django.contrib import admin


urlpatterns = [
    re_path(r'^register/$', RegistrationView.as_view(), name='register'),
    re_path(r'^auth/$', AuthenticationView.as_view(), name='auth'),
    re_path(r'^logout$', logout_view, name='logout'),
    re_path(r'^scan/', ScanView.as_view(), name='scan'),
]