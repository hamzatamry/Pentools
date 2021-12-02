from django.urls import path
from .views import *



urlpatterns = [
    path(r'register/', Registration.as_view()),
]