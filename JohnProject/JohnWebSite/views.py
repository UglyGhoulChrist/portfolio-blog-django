from django.shortcuts import render
from .models import ExtUser, Social, Blog, Project

if ExtUser.objects.exists():
    extUser = ExtUser.objects.first()  


blogs = Blog.objects.all()    
socials = Social.objects.all()    
projects = Project.objects.all()    

def home(request):
    return render(request, 'JohnWebSite/home.html', {'link':1,'extUser':extUser,'blogs':blogs,'projects':projects,})


def blogs(request):
    return render(request, 'JohnWebSite/blogs.html',{'link':2,'blogs':blogs,})


def works(request):
    return render(request, 'JohnWebSite/works.html',{'link':3,'projects':projects,})
