from django.shortcuts import render

# Create your views here.

def login_view(request):
    context = {
        'title': "Login"
    }
    return render(request, 'login.html', context)

def register_view(request):
    context = {
        'title': "Register"
    }
    return render(request, 'register.html', context)

def logout_user(request):
    return