from django.shortcuts import render

# Create your views here.

def loginView(request):
    context = {
        'title': "Login"
    }
    return render(request, 'login.html', context)

def registerView(request):
    context = {
        'title': "Register"
    }
    return render(request, 'register.html', context)

def logoutUser(request):
    return