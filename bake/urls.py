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
    path('logout', views.logout),
    path('edit_profile', views.editprofile),
    path('newrecipe', views.newrecipe),
    path('adding', views.adding),
    path('recipe/<int:num>', views.recipe)
]