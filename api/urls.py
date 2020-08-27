from django.contrib import admin
from django.urls import path,include

from .views import register,signin,users_info,add_blogs

urlpatterns =[
    path('register/',register,name="user-register"),
    path('signin/',signin,name="user-signin"),
    path('users_info/',users_info,name="user-info"),
    path('add_blogs/',add_blogs,name="add-blogs")
]