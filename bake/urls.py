from django.urls import path
from.import views

urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('registration', views.registration),
    path('homepage', views.homepage),
    path('profile', views.profile),
    path('my_recipes', views.my_recipes),
]