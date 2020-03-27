from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return HttpResponse("Welcome to app 2 index page")
def contact(request):
    return HttpResponse("Welcome to app 2 CONTACT page")
def home(request):
    return redirect("/")
def name(request, name):
    return HttpResponse(f"Welcome to blog name: {name}")