from ast import Delete
from django.urls import path
from .views import *
urlpatterns = [
      path('index1',index),
    #   path('index2',index2),
    path('update/<str:pk>/', update, name= "update"),
    path('delete_task/<str:pk>/', delete_task, name = "delete_task"),

       
  ]