from django.shortcuts import render, redirect
from time import strftime, gmtime

def index(request):
    if 'words' not in request.session:
        request.session['words'] = []
    context = {
        'words': request.session['words']
        }
    return render(request, "index.html", context)

def process(request):
    if 'words' not in request.session:
        return redirect("/sessionwords/")
    if 'color' not in request.POST:
        color = 'black'
    else:
        color = request.POST['color']
    if 'big' in request.POST:
        size = '20'
        weight = 'bold'
    else:
        size = '12'
        weight = 'normal'
    time = str(strftime("%Y-%m-%d %H:%M %p", gmtime()))
    newword = {
            'word': request.POST['word'],
            'color': color,
            'size': size,
            'weight': weight,
            'createdat': time
        }
    request.session['words'] = request.session['words'] + [newword]
    return redirect("/sessionwords/")

def clear(request):
    if 'words' in request.session:
        del request.session['words']
    return redirect("/sessionwords")