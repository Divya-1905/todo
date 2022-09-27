from ast import Delete
from django.urls import path
from .views import *
urlpatterns = [
      path('index',index, name= "index"),
    path('update/<str:pk>/', update, name= "update"),
    path('delete_task/<str:pk>/', delete_task, name = "delete_task"),

       
  ]