from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    request.session['counter'] = 0
    return render(request, "random_word.html")

def random_word(request):
    request.session['counter'] = request.session['counter'] + 1
    request.session['word'] = get_random_string(length=14)
    return render(request, "random_word.html")

def reset(request):
    request.session.flush()
    return redirect('/')

