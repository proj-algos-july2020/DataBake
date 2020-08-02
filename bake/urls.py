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
    path('recipe/<int:num>', views.recipe),
    path('doughs', views.doughs),
    path('creams', views.creams),
    path('mousses', views.mousses),
    path('glazes', views.glazes),
    path('sponges', views.sponges),
    path('syrups', views.syrups),
    path('confection', views.confection),
    path('other', views.other),
]