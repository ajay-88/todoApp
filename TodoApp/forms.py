from django import forms
from django.contrib.auth.models import User
from TodoApp.models import Task
class Register(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password','first_name','last_name','email']


class Signin(forms.Form):
    Username=forms.CharField()
    Password=forms.CharField()


class Taskform(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name']


