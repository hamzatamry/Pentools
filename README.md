# Pen-tools

Application Web permettant l'application des tests d'intrusion.

#   Guide

>   To create a django app we need at first install it's framework

>   We can install it globally on the machine which is not recommended because for some project we may need different django versions. 

>   So we have to create a virtual environement on which we gonna install our django.

1.  navigate to your project folder

2.  open your command prompt (windows)

3.  run this command
```
    python -m venv <nameOfvirtualEnvironement>
```
4.  Then we type this next command to activate the virtual environement
```
    <nameOfvirtualEnvironement>\Scripts\activate
```
5.  We type this command to install django on our virtual environement
```
    pip install Django
```
6. To create a Django project we type this command:
```
    django-admin startproject <projectName> .
```
>   Notice: new folder created with some bunch of python files a manage.py file is created

7.  To run the Django server we type this command
```
    python manage.py runserver
```

>   If you don't want to repeat the command each time, you can open the project folder with PyCharm IDE, and run manage.py, then go to edit configurations, and put runserver as a parameter, then you can run the server by only pressing the run button.

8.  Until now we have only created a django project, bascially a django project can contain multiple apps, so to create an App we run this command in terminal
```
    django-admin startapp <appName>
```
9. run this command to migrate modifications and installations to database
```
    python manage.py migrate 
```
10. To see what is in our database as an administrator, we can create a user admin with this command
```
    python manage.py createsuperuser
```
11. create a Model in model.py then run these two commands
```
    python manage.py makemigrations
    python manage.py migrate
```
12. add these two lines of code to admins.py where model is the name of the Model 
```py
    from .models import Model
    admin.site.register(Model)
```

##  Adding Mysql as a database and configuring django project settings

1. Make sure you have installed python and Django framework (globally or on a virtual environement)

2. Check the version of your python by running on terminal or command prompt this command
```
    python
```

3. Install MySQL by downloading it from it's official site.

>   during the installation a useradmin and password are required, make sure you keep them in mind and not forget them.

4. Configure MySQL with Django by changing DATABASES Constant in setting.py to this
```py
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'USER': '<username>',
            'NAME': '<database name>',
            'PASSWORD': '<your paswword that you have entered>',
            'PORT': '5432'
        }
    }
```
##  Installing Django-Rest Framework

1.  We run this command to install django rest frameword (make sure you have activated the virtual environement)
```
pip install djangorestframework
```
2. Then you should add it to INSTALLED_APPS in settings.py
```py
INSTALLED_APPS = [
	...
	'rest_framework'
]
```