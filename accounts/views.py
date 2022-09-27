from django.shortcuts import render, redirect
from django import forms 
from .models import*
from .form import loginform, signupform
from django.contrib.auth import authenticate,login

# Create your views here.
def signup(request):
    form=signupform()
    if request.method=='POST':
        signupform1 = signupform(request.POST)
        print(request.POST)
        if signupform1.is_valid():
            print('hi')
            signupform1.save()
            
    return render (request,'accounts/accounts.html',{'form':form} )   
def signin(request):
    form=loginform()
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=authenticate(request,username=email,password=password)
        print(user)
        if user:
            print(user)
            login(request,user)
            return redirect ('index')
        
    return render(request,'accounts/login.html',{'form':form})    

        
        
        
       
    
    
    
    
    
    
    
        
