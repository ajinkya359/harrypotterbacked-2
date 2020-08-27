from django.contrib import admin
from django.urls import path,include

from .views import register,signin,users_info,add_blogs,create_groups,get_groups

urlpatterns =[
    path('register/',register,name="user-register"),
    path('signin/',signin,name="user-signin"),
    path('users_info/',users_info,name="user-info"),
    path('add_blogs/',add_blogs,name="add-blogs"),
    path('create_groups/',create_groups,name="new-group"),
    path('get_groups/', get_groups, name="get-groups"),

]