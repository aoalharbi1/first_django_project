from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect("/")

def show(request, num):
    return HttpResponse("placeholder to display blog number: " + num)

def edit(request, num):
    return HttpResponse("placeholder to edit blog " + num)

def destroy(request, num):
    return redirect("/")