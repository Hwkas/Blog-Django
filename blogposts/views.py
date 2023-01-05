from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .models import *
from .forms import *
from datetime import datetime
from .decorators import *

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


@login_required(login_url="login")
def create_post(request):
    form = CreatePostForm()
    if request.method == "POST":
        form = CreatePostForm(request.POST)
        if form.is_valid():
            # we need to modify the form like this to add any field which is exclude in the form.
            modified_form = form.save(commit=False)
            user = request.user
            modified_form.author = user
            modified_form.save()
            return redirect(home)
    year = datetime.now().year
    context = {"form": form, "year": year}
    return render(request, 'blogposts/create-post.html', context)


@login_required(login_url="login")
def edit_post(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    form = CreatePostForm(instance=post)
    if request.method == "POST":
        form = CreatePostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect(home)
    year = datetime.now().year
    context = {"form": form, "year": year}
    return render(request, 'blogposts/create-post.html', context)


@login_required(login_url="login")
def delete_post(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    post.delete()
    return redirect(home)


@unauthenticated_user
def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name="customer")
            user.groups.add(group)
            # username = form.cleaned_data.get("username")
            # messages.success(request, username + " you account has been created successfully")
            return redirect(home)
    year = datetime.now().year
    context = {"form": form, "year": year}
    return render(request, 'blogposts/register.html', context)


@unauthenticated_user
def login_page(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = form.data["username"]
        password = form.data["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(home)
        else:
            messages.info(request, "Username OR Password is incorrect")
    year = datetime.now().year
    context = {"form": form, "year": year}
    return render(request, 'blogposts/login.html', context)


def logout_page(request):
    logout(request)
    return redirect(home)


def about(request):
    year = datetime.now().year
    context = {"year": year}
    return render(request, 'blogposts/about.html', context)


@allowed_user(allowed_roles=["admin"])
def contact(request):
    year = datetime.now().year
    context = {"year": year}
    return render(request, 'blogposts/contact.html', context)
