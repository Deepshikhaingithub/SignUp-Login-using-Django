from collections import UserDict, UserString
import email
from django.conf import UserSettingsHolder
from django.shortcuts import redirect, render
from django.contrib.auth.models import User

# Create your views here.
from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse, redirect


def signup(request):
        if request.method== "POST":
            username=request.POST['username']
            firstname= request.POST['first_name']
            lastname=request.POST['last_name']
            email=request.POST['email']
            password=request.POST['password']

            x=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
            x.save()
            print("User created")
            return redirect('/')
        else:
            return render(request, 'form.html')

