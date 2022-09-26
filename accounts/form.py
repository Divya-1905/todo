from dataclasses import fields
import email
from accounts.models import  user
from django import forms 


class signupform(forms.ModelForm):
    class Meta:
        model=user
        fields=['password','email','phone']
    def save(self, commit=True):
       # Save the provided password in hashed format
       user = super().save(commit=False)
       user.set_password(self.cleaned_data["password"])
    #    if commit:
       user.save()
       return user
class loginform(forms.ModelForm):
    class Meta:
        model=user
        fields=['email','password']        