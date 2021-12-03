from django.urls import path, re_path
from .views import *
from django.contrib import admin


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^register/$', Registration.as_view(), name='register'),
    re_path(r'^auth/$', Authentication.as_view(), name='auth'),
    re_path(r'^logout$', logout_view, name='logout'),
]