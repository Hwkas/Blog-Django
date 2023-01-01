from django.shortcuts import render, redirect

from django.http import HttpResponse
from .models import * 
from .forms import *
from datetime import datetime

# Create your views here.

def home(request):
    all_posts = BlogPost.objects.all
    year = datetime.now().year
    context = {"all_posts": all_posts, "year": year}
    return render(request, 'blogposts/index.html', context)

def post(request, post_id):
    curr_post = BlogPost.objects.get(id=post_id)
    year = datetime.now().year
    context = {"post": curr_post, "year": year}
    return render(request, 'blogposts/post.html', context)

def create_post(request):
    form = CreatePostForm()
    if request.method == "POST":
        form = CreatePostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(home)
    year = datetime.now().year
    context = {"form": form, "year": year}
    return render(request, 'blogposts/make-post.html', context)

def edit_post(request, post_id):
    post = BlogPost.objects.get(id=post_id )
    form = CreatePostForm(instance=post)
    if request.method == "POST":
        form = CreatePostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect(home)
    year = datetime.now().year
    context = {"form": form, "year": year}
    return render(request, 'blogposts/make-post.html', context)

def delete_post(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    post.delete()
    return redirect(home)

def login(request):
    year = datetime.now().year
    context = {"year": year}
    return render(request, 'blogposts/login.html', context)

def logout(request):
    return redirect(home)

def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(home)
    year = datetime.now().year
    context = {"form": form, "year": year}
    return render(request, 'blogposts/register.html', context)

def about(request):
    year = datetime.now().year
    context = {"year": year}
    return render(request, 'blogposts/about.html', context)

def contact(request):
    year = datetime.now().year
    context = {"year": year}
    return render(request, 'blogposts/contact.html', context)

