from dataclasses import fields
from pyexpat import model
from socket import fromshare
from django import forms
from.models import Todo
class Todoform(forms.ModelForm):
    class Meta:
        model = Todo
        fields="__all__"
        exclude=['user']
    def save(self, user,commit=True):
           # Save the provided password in hashed format
       todo= super().save(commit=False)
       todo.user=user
    #    if commit:
       todo.save()