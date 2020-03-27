from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if request.method == "GET":
        print("GET")
        return render(request, 'index.html')
    if request.method == "POST":
        print("POST")
        return redirect("result")

def result(request):
    if request.method == "POST":
        context = {
            'name': request.POST["name"],
            'location': request.POST["location_list"],
            'language': request.POST["language_list"],
            'comment': request.POST["comment"]
        }
        return render(request, 'result.html', context)
