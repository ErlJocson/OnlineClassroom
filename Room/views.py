from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Room

@login_required
def homeView(request):
    # filter this rooms per current user
    rooms = Room.objects.all()
    createdRooms = Room.objects.filter(teacher=request.user.id)
    context = {
        'title':'Rooms',
        'rooms':rooms,
        "createdRooms":createdRooms,
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
    if request.method == 'POST':
        roomName = request.POST['roomName']
        description = request.POST['description']

        roomToCreate = Room.objects.create(
            name = roomName,
            description = description,
            teacher = request.user,
        )
        roomToCreate.save()
        return redirect('home')

    context = {
        'title':'Create room'
    }
    return render(request, 'createRoom.html', context)

def roomView(request, roomId):
    roomToView = Room.objects.get(id=roomId)
    context = {
        'title':'Room view',
        "room":roomToView,
    }
    return render(request, 'roomView.html', context)