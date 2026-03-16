from django.shortcuts import render, redirect
import random
from datetime import datetime

# Create your views here.
def index(request):
    if 'game' not in request.session:
        request.session['game'] = False
        request.session['game_over'] = False
        request.session['gold'] = 0
        request.session['moves'] = 0
        request.session['goal'] = 0
        request.session['max_moves'] = 0
        request.session['activities'] = []
        request.session['result'] = ""

    return render(request, "index.html")

def start_game(request):
    if request.method == 'POST':
        request.session['game'] = True
        request.session['game_over'] = False
        request.session['gold'] = 0
        request.session['moves'] = 0
        request.session['goal'] = int(request.POST['goal'])
        request.session['max_moves'] = int(request.POST['max_moves'])
        request.session['activities'] = []
        request.session['result'] = ""
    
    return redirect('/')

def process_money(request):
    if request.session['game_over']:
        return redirect ('/')
    
    location = request.POST['location']
    if location == 'farm':
        gold_change = random.randint( 10 ,20 )
    elif location == 'cave':
        gold_change = random.randint( 10 , 20 )
    elif location == 'house':
        gold_change = random.randint( 10 , 20 )
    elif location == 'quest':
        gold_change = random.randint( -50 , 50 )

    request.session['gold'] += gold_change
    request.session['moves'] += 1

    date_time = datetime.now().strftime("%B %d %Y %I:%M:%p")

    if gold_change >= 0:
        action = "earned"
    else:
        action = "lost"

    message = f"You entered a {location} and {action} {abs(gold_change)} gold. ({date_time})"

    activity ={
        "message" : message,
        "gold" : gold_change
    }

    activities = request .session['activities']
    activities.insert(0, activity)
    request.session['activities'] = activities

    if request.session['gold'] >= request.session['goal']:
        request.session['game_over'] = True
        request.session['result'] = "Congrats! You win"
    elif request.session['moves'] >= request.session['max_moves']:
        request.session['game_over'] = True
        request.session['result'] = "Game Over! You are out of moves"

    return redirect ('/')

def reset(request):
    request.session.flush()
    return redirect('/')

