from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def process(request):
    if request.method != "POST":
        return redirect('/')
    print(request.POST)
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location_list']
    request.session['language'] = request.POST['language_list']
    request.session['comment'] = request.POST['comment']
    return redirect('/result')

def result(request):
    return render(request, 'result.html')

def clear_session(request):
    request.session.flush()
    return redirect('/')