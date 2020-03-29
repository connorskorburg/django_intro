from django.shortcuts import render, redirect, HttpResponse
import random
from time import gmtime, strftime
# Create your views here.

def index(request):
    if 'gold_amount' not in request.session or 'gold_display' not in request.session:
        request.session['gold_amount'] = 0 
        request.session['gold_display'] = []
    return render(request, 'index.html')


def process(request):
    print(request.POST)
    if request.method == "GET":
        return redirect('/')
    if 'farm' in request.POST:
        gold = random.randint(10, 20)
        request.session['gold_amount'] = request.session['gold_amount'] + gold
        request.session['gold_display'].append( f"Earned {str(gold)} golds from the farm! ({strftime('%I:%M %p', gmtime())})")
        return redirect('/')
    if 'cave' in request.POST:
        gold = random.randint(5, 10)
        request.session['gold_amount'] = request.session['gold_amount'] + gold
        request.session['gold_display'].append( f"Earned {str(gold)} golds from the cave! ({strftime('%I:%M %p', gmtime())})")
        return redirect('/')
    if 'house' in request.POST:
        gold = random.randint(2, 5)
        request.session['gold_amount'] = request.session['gold_amount'] + gold
        request.session['gold_display'].append( f"Earned {str(gold)} golds from the house! ({strftime('%I:%M %p', gmtime())})")
        return redirect('/')
    if 'casino' in request.POST:
        gold = random.randint(-50, 50)
        request.session['gold_amount'] = request.session['gold_amount'] + gold
        if gold >= 0:
            request.session['gold_display'].append( f"Earned {str(gold)} golds from the casino! ({strftime('%I:%M %p', gmtime())})")
            return redirect('/')
        else:
            request.session['gold_display'].append(f"Lost {str(gold)} golds from the casino! ({strftime('%I:%M %p', gmtime())})")
            return redirect('/')
#reset session
def clear_session(request):
    request.session.flush()
    return redirect('/')