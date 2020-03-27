from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return HttpResponse("Welcome to app 1 index page")
def about(request):
    return HttpResponse("Welcome to app 1 ABOUT page")
def blog_num(request, number):
    return HttpResponse(f"Welcome to blog number: {number}")
