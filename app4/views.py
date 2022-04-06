from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from collections import UserDict, UserString
import email
from django.conf import UserSettingsHolder
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth

# Create your views here.
from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse, redirect


def logout(request):
    auth.logout(request)
    return redirect('/')
        
