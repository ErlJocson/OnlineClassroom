from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')

    context = {
        'title': "Login"
    }
    return render(request, 'login.html', context)

def registerView(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(
            username=username,
            first_name=firstName,
            last_name=lastName,
            email=email,
            password=password
        )
        user.save()
        login(request, authenticate(request, username=username, password=password))
        return redirect('home')

    context = {
        'title': "Register"
    }
    return render(request, 'register.html', context)

@login_required
def logoutUser(request):
    logout(request)
    return redirect('login')