from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django import forms
from  . models import Dsa
class SignUpForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name',"last_name","username","password"]


class DsaForm(forms.ModelForm):
    class Meta:
        model=Dsa
        fields="__all__"
