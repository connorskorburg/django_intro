from django.shortcuts import render, redirect, HttpResponse
# Create your views here.

def index(request):
    return render(request, "index.html")

def process(request):
    if request.method != "POST":
        return redirect("/")
    request.session['username'] = request.POST['username']
    request.session['email']  = request.POST['email']
    request.session['password']  = request.POST['password']
    request.session['fav_num'] = 100
    return redirect('/results')

def results(request):
    if 'fav_num' not in request.session:
        return redirect('/')
    return render(request, "results.html")

def clear_session(request):
    request.session.flush()
    return redirect('/')