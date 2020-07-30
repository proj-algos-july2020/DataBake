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

            request.session['id'] = user.id 
            return redirect('/user')
    return redirect('/')

def registration(request):
    return render(request, 'registration.html')

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/registration')

    hash_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()

    user=User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], city=request.POST['city'], state=request.POST['state'],zipcode=request.POST['zipcode'], title=request.POST['title'],bio=request.POST['bio'], user_name=request.POST['user_name'], password=hash_pw)

    request.session['name']=user.first_name
    request.session['id'] = user.id 
    return redirect('/user')

def user(request):
    return render(request, 'profile.html')

