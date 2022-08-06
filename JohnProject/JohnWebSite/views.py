from django.shortcuts import render
from .models import ExtUser, Social, Blog, Project

if ExtUser.objects.exists():
    extUser = ExtUser.objects.first()  

def home(request):
    return render(request, 'JohnWebSite/home.html', {'link':1,'extUser':extUser})


def blogs(request):
    return render(request, 'JohnWebSite/blogs.html',{'link':2,})


def works(request):
    return render(request, 'JohnWebSite/works.html',{'link':3,})
