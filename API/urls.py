from django.urls import path
from .views import *


urlpatterns = [
    path('register/', Registration.as_view()),
]