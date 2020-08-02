from django.urls import path
from.import views

urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('registration', views.registration),
    path('register', views.register),
    path('homepage', views.homepage),
    path('profile/<int:id>', views.profile),
    path('my_recipes', views.my_recipes),
    # path('rImageUpload', views.rImageUpload),
    path('profpic', views.profpic),
    path('profpic/<int:id>', views.profile_upload),
]