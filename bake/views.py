from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
import bcrypt
import math
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

    if 'id' not in request.session:
        return redirect('/')
    context = { 
        'logged_user' : User.objects.get(id=request.session['id']),
        }
    print(context['logged_user'])


    return render(request, 'profile.html', context)

def editprofile(request):
    return render (request,'edit_profile.html')

def homepage(request):
    return render(request, 'homepage.html')

def profile(request):
    return render(request, 'profile.html')

def my_recipes(request):
    context = {
        'recipes': Recipe.objects.all()
    }
    return render(request, 'my_recipes.html', context)

def create(request):
    return render(request, 'recipe.html')

def logout(request):
    request.session.clear()
    return redirect('/')

def newrecipe(request):
    if request.method == 'POST':
        for key, values in request.POST.lists():
            if key == 'qty':
                qtyv = values
            if key == 'meas':
                measv = values
            if key == 'ingredient':
                ingv = values
    
        user = User.objects.get(id=request.session['id'])
        newRecipe = Recipe.objects.create(recipe_title=request.POST['title'], recipe_directions=request.POST['dir'], category=request.POST['category'],uploaded_by=user)

        for i in range(len(qtyv)):
            if qtyv[i] != "":
                Ingredient.objects.create(ingredient_name=ingv[i],ingredient_quantity=qtyv[i],ingredient_measurement=measv[i], ingredients_for=newRecipe)
                
        return redirect(my_recipes)
    return redirect(create)

def adding(request):
    return render(request, 'add_ingredient.html')

def recipe(request, num):
    context = {
        'recipe': Recipe.objects.get(id=num)
    }
    return render(request, 'recipe_info.html', context)

