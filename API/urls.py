from django.urls import path
from .views import *


urlpatterns = [
    path('register/', Registration.as_view()),
    path('auth/', Authentication.as_view()),
    path('scan/', Scan.as_view())
]