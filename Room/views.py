from django.shortcuts import render

def homeView(request):
    context = {
        'title':'Rooms'
    }
    return render(request, 'home.html', context)

def missingView(request):
    context = {
        'title':'Missing'
    }
    return render(request, 'missing.html', context)

def todoView(request):
    context = {
        'title':'Todo'
    }
    return render(request, 'todo.html', context)

def doneView(request):
    context = {
        'title':'Done'
    }
    return render(request, 'done.html', context)