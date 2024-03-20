from django.shortcuts import render,redirect
from django.views.generic import View
from TodoApp.forms import Register,Signin,Taskform
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from TodoApp.models import Task
from django.contrib import messages
from django.utils.decorators import method_decorator


def sigin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        else:
            return fn(request,*args,**kwargs)
    return wrapper


def mylogin(fn):
    def wrapper(request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Task.objects.get(id=id)
        if obj.user != request.user:
            return redirect("login")
        else:
            return fn(request,*args,**kwargs)
    return wrapper

# Create your views here.

class Registerview(View):
    def get(self,request,*args,**kwargs):
        form=Register()
        return render(request,"reg.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=Register(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)  #saving then password encryption
            # form.save()  #store the data into database
            print(form.cleaned_data)   #terminal data printing
        else:
            print("ERROR")
        form=Register()
        return render(request,"reg.html",{"form":form})
    
class Signview(View):
    def get(self,request,*args,**kwargs):
        form=Signin()
        return render(request,"login.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=Signin(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            user_name=form.cleaned_data.get("Username")
            pass_word=form.cleaned_data.get("Password")
            User_obj=authenticate(request,username=user_name,password=pass_word)
            if User_obj:
                print(User_obj)
                print("Valid Credential")
                login(request,User_obj)
                return redirect("index")
            else:
                print("Invalid Credential")
        else:
            print("Error found..Please checkout it...")
        return render(request,"login.html",{"form":form})

# @method_decorator(sigin_required,name="dispatch")      #already login aya allk mathram view page kannan decrator create cheyyanm
class Taskview(View):
    def get(self,request,*args,**kwargs):
        form=Taskform()
        data=Task.objects.filter(user=request.user).order_by('complete')
        return render(request,"index.html",{"form":form,"data":data})
    
    def post(self,request,*args,**kwargs):
        form=Taskform(request.POST)
        if form.is_valid():
            form.instance.user=request.user
            form.save()
        else:
            print("Error found")
        form=Taskform()
        data=Task.objects.filter(user=request.user)
        messages.success(request,"Task added successfully")
        return render(request,"index.html",{"form":form,"data": data})

@method_decorator(mylogin,name="dispatch")
class Taskupdate(View):
    # def get(self,request,*args,**kwargs):
    #     id=kwargs.get("pk")
    #     Task.objects.filter(id=id).update(complete=True)
    #     messages.success(request,"Task edited successfully")
    #     return redirect("index")    
    # task true only

    # true and false statement case

    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Task.objects.get(id=id)
        if qs.complete == True:
            qs.complete = False
            qs.save()
        elif qs.complete == False:
            qs.complete = True
            qs.save()

        return redirect("index")

    
@method_decorator(mylogin,name="dispatch")
class Taskdelete(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Task.objects.filter(id=id).delete()
        messages.error(request,"Task deleted successfully")
        return redirect("index")



class Signout(View):
    def get(self,request):
        logout(request)
        return redirect("login")


# user deletion
class User_del(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        User.objects.get(id=id).delete()
        return redirect("reg")