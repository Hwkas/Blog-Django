from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'blogposts/index.html')

def login(request):
    return render(request, 'blogposts/login.html')

def register(request):
    return render(request, 'blogposts/register.html')

def about(request):
    return render(request, 'blogposts/about.html')

def contact(request):
    return render(request, 'blogposts/contact.html')

