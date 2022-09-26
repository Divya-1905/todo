from audioop import add
from email.policy import default
from pickle import TRUE
from re import T
from django.db import models
from accounts. models import user
from django.contrib.auth.models import BaseUserManager , AbstractBaseUser
# Create your models here.

class Todo (models.Model):
   user = models.ForeignKey(user,on_delete=models.CASCADE,null=True)
   tittle=models.CharField(max_length=35)
   details = models.TextField()
#    date = models.DateField(auto_now_add=True)
   complete = models.BooleanField(default=False)
   takenHours = models.IntegerField(default=0,blank=True)
   created = models.DateTimeField(auto_now_add=True)
   notification = models.CharField(max_length=34,blank=True)
   plannedhours = models.IntegerField(default=0,blank=True)
   def  __str__(self):
       return self.tittle
     
    

    
