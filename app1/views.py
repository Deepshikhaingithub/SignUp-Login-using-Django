from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse


# Create your views here.

from django.http import HttpResponse

def index(request):
    return render(request, 'design.html', {'link' :'http://127.0.0.1:8000/'})

def profile(request):
    return render(request, 'dynamic.html', {'titles' :'This is a profile page', 'link' :'http://127.0.0.1:8000/'})

def about(request):
    return HttpResponse("Congrats! You did it")

def form(request):
    return render(request, 'design.html', {'link' :'http://127.0.0.1:8000/'})

def expression(request):
    a= int(request.GET['text1'])
    b= int(request.GET['text2'])
    c= a+2*b
    return render(request, 'output.html', {'result': c})




