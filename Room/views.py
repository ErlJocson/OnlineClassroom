from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def homeView(request):
    context = {
        'title':'Rooms'
    }
    return render(request, 'home.html', context)

@login_required
def missingView(request):
    context = {
        'title':'Missing'
    }
    return render(request, 'missing.html', context)

@login_required
def todoView(request):
    context = {
        'title':'Todo'
    }
    return render(request, 'todo.html', context)

@login_required
def doneView(request):
    context = {
        'title':'Done'
    }
    return render(request, 'done.html', context)

@login_required
def createRoom(request):
    context = {
        'title':'Create room'
    }
    return render(request, 'createRoom.html', context)