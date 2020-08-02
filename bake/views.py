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
            # return redirect('/user')
    return redirect('/homepage')

def user(request):

    if 'id' not in request.session:
        return redirect('/')
    context = { 
        'logged_user' : User.objects.get(id=request.session['id']),
        }
    print(context['logged_user'])


    return render(request, 'profile.html', context)

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

def homepage(request):
    context = {
        "user": User.objects.get(id=request.session['id']),
    }
    return render(request, 'homepage.html', context)

def profile(request, id):
    context = {
        "user": User.objects.get(id=request.session['id']),
    }
    return render(request, 'profile.html', context)

def my_recipes(request):
    return render(request, 'my_recipes.html')
    
def profpic(request):
    # To edit profile picture
    context = {
        "user": User.objects.get(id=request.session['id']),
    }
    return render(request, 'photo_upload.html', context)

def profile_upload(request, id):
    # To upload new photo as profile photo - add to imagefield in User model
    updated = User.objects.get(id=id)
    if request.method == "POST":
        updated.image = request.FILES['profile_photo']
    updated.save()
    return redirect(f'/profile/{id}')