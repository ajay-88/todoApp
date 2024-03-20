"""
URL configuration for TODO project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from TodoApp.views import Registerview,Signview,Signout,Taskview,Taskupdate,Taskdelete,User_del
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Registerview.as_view(),name='reg'),
    path('login/',Signview.as_view(),name="login"),
    path('logout/',Signout.as_view(),name="logout"),
    path('index/',Taskview.as_view(),name='index'),
    path('edit/<int:pk>',Taskupdate.as_view(),name='edit'),
    path('delete/<int:pk>',Taskdelete.as_view(),name='del'),
    path('del/<int:pk>',User_del.as_view(),name='userdel'),

    
]
