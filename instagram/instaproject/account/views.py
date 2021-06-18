from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.


def signup_view(request):
    if request.method == 'POST':
        user = User.objects.create_user(
            email=request.POST["email"], username=request.POST["username"], password=request.POST["password"])
        auth.login(request, user)
        return redirect('feed')
    return render(request, 'signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('feed')
        else:
            return render(request, 'login.html', print("user is none"))
    else:
        return render(request, 'login.html')


def logout_view(request):
    auth.logout(request)
    return redirect('feed')