from instaproject import instagram
from django.shortcuts import render, redirect, get_object_or_404
from .models import Websta
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def home(request):
    return render(request,'feed.html')

def profile(request):
    return render(request,"profile.html")

def feed(request):
    return render(request,"feed.html")

def base(request):
    return render(request,"base.html")    

def new(request):
    return render(request, 'new.html')

def create(request):
    new_post = instagram()
    new_post.writer = request.user
    new_post.image = request.FILES['image']
    new_post.save()
    return redirect('feed')    

def edit(request, id):
    edit_post = instagram.objects.get(id=id)
    return render(request, 'edit.html', {'post': edit_post})


def update(request, id):
    update_post = instagram.objects.get(id=id)
    update_post.writer = request.user
    update_post.image = request.FILES['image']
    update_post.save()
    return redirect('feed')


def delete(request, id):
    delete_post = instagram.objects.get(id=id)
    delete_post.delete()
    return redirect('feed')
