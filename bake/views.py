from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
import bcrypt
def index(request):
    return render(request, 'index.html')

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    user = User.objects.filter(user_name=request.POST['user_name'])
    if user:
        user = user[0]
        if bcrypt.checkpw(request.POST['password_input'].encode(), user.password.encode()):
            request.session['first_name'] = user.first_name
            request.session['id'] = user.id 
            return redirect('/user')
    return redirect('/')

def registration(request):
    return render(request, 'register.html')

def homepage(request):
    return render(request, 'homepage.html')

def profile(request):
    return render(request, 'profile.html')

def my_recipes(request):
    return render(request, 'my_recipes.html')
