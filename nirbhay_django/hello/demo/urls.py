from django.contrib import admin  
from django.urls import path,include
from .views import *  #import views fille


urlpatterns = [
    
    path('',nk),              # api name and fantionname
    # path('abc/',jojo),        # api 2 name and fantionname
    path('post/',rk),         # api name and fantionname
    path('put/<id>/',nk1),    # api name and fantionname
    path('patch/<id>/',nk2),  # api name and fantionname
    path('delete/<id>/',nk3)  # api name and fantionname
    
]
