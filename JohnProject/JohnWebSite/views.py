from django.shortcuts import render
from .models import ExtUser, Social, Blog, Project

if ExtUser.objects.exists():
    extUser = ExtUser.objects.first()

blogs = Blog.objects.all()
socials = Social.objects.all()
projects = Project.objects.all()

def showHome(request):
    return render(request, 'JohnWebSite/home.html',
                  {'link': 1, 'extUser': extUser, 'blogs': blogs, 'projects': projects, })


def showBlogs(request):
    return render(request, 'JohnWebSite/blogs.html', {'link': 2, 'blogs': blogs, })


def showWorks(request):
    return render(request, 'JohnWebSite/works.html', {'link': 3, 'projects': projects, })
