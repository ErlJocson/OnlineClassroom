from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Room, ListOfStudent
from Requirement.models import TeacherPost
from django.contrib import messages

@login_required
def homeView(request):
    rooms = ListOfStudent.objects.filter(student=request.user.id)
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
def joinRoomView(request):
    if request.method == 'POST':
        roomName = request.POST['roomName']
        roomId = request.POST['roomId']

        checkIfRoomExist = Room.objects.filter(name=roomName, roomId=roomId)
        print(checkIfRoomExist)
        if checkIfRoomExist.first():
            # check if student is already joined
            newStudent = ListOfStudent.objects.create(
                room=checkIfRoomExist,
                student=request.user
            )
            newStudent.save()
            messages.success(request, 'Joined a room')
        else:
            messages.warning(request, 'Room does not exist. There might be a typing error')
    context = {
        'title':'Join'
    }
    return render(request, 'joinRoomView.html', context)

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
        messages.success(request, 'Created a room')
        return redirect('home')

    context = {
        'title':'Create room'
    }
    return render(request, 'createRoom.html', context)

def roomView(request, roomId):
    roomToView = Room.objects.get(id=roomId)
    teacherPosts = TeacherPost.objects.filter(teacher = request.user.id, room = roomToView.id)
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        date = request.POST['date']
        toBeSubmitted = request.POST['toBeSubmitted']
        newPost = TeacherPost.objects.create(
            title = title, 
            description = description, 
            deadline = date, 
            toBeSubmitted = toBeSubmitted,
            teacher = request.user,
            room = roomToView
        )
        newPost.save()
    context = {
        'title':roomToView.name,
        "room":roomToView,
        'teacherPosts':teacherPosts,
    }
    return render(request, 'roomView.html', context)