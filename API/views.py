from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class Registration(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

    def post(self, request, *args, **kwargs):
        print(request.method)
        #   Registration
        return HttpResponse("<h1>POST /register/</h1>")

    def put(self, request, *args, **kwargs):
        return HttpResponse("<h1>PUT is NOT ALLOWED /register/</h1>")

    def delete(self, request, *args, **kwargs):
        return HttpResponse("<h1>DELETE is NOT ALLOWED /register/</h1>")

