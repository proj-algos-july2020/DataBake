from django.urls import path
from.import views

urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('registration', views.registration),
    path('register', views.register),
    path('user', views.user),
    path('homepage', views.homepage),
    path('profile', views.profile),
    path('my_recipes', views.my_recipes),
    path('create', views.create),
    path('newrecipe', views.newrecipe),
    path('ingredients', views.ingredients),
    path('adding', views.adding),
    path('recipe/<int:num>', views.recipe)
]