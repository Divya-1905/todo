


from asyncio import Task
from contextvars import Context
from multiprocessing import context
from django.http import HttpResponse

from .models import *
from django.shortcuts import render,redirect
from .form import Todoform
# Create your views here.
def index(request):
    form1= Todoform()
    user=request.user
    data = Todo.objects.filter(user=request.user)
    # item_list = Todo.objects.order_by("_date")
    if request.method =="POST":
         print(request.user,'hi')
         form1 = Todoform(request.POST)
         if form1.is_valid():
             form1.save(request.user)
             
            #  return redirect('Todo') 
        
    return render(request,'todoapp/list.html',{'form':form1,'data':data,'user':user} )

def update(request,pk):
    data = Todo.objects.get(id=pk)
    form = Todoform(instance=data)
    if request.method =="POST":
        form = Todoform(request.POST,instance=data)
        if form.is_valid():
            # data.complete = data.takenHours + data.plannedhours 
            form.save(request.user,commit=False)
        return redirect('index')
    context = {'form':form}
    return render(request,'todoapp/update.html',context)
def delete_task(request, pk):
    task = Todo.objects.get(id=pk)
    if request.method =="POST":
       task.delete()
       return redirect('index')
    # context = {'form':task}        
    return render(request,'todoapp/delete.html',{})       
