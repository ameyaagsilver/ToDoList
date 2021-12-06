"""ToDoList URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from Login import views

urlpatterns = [
    path('', views.testLogin, name="testLogin"),
    path('login/', views.login, name="login"),
    path('testData/', views.testData, name = "testing"),
    path('postLogin/', views.postLogin, name = "postLogin"),
    path('logout/', views.logout, name = "logout"),
    path('testSignUp/', views.testSignUp, name = "signUp"),
    path('postSignUp/', views.postSignUp, name = "postSignUp"),
    # path('testingSessionId/', views.testingSessionId, name="testingSessionId"),
    path('toDoList/', views.toDoList, name="toDoList"),
    path('addData/', views.addData, name="addData"),
    path('deleteData/', views.deleteData, name="deleteData")
]
