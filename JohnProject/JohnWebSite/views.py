from django.shortcuts import render
from .models import ExtUser, Social, Blog, Project

if ExtUser.objects.exists():
    extUser = ExtUser.objects.first()


socials = Social.objects.all()


def showHome(request):
    blogs = Blog.objects.filter(activeBlog=True)[:2]
    projects = Project.objects.filter(activeProject=True)[:3]
    return render(request, 'JohnWebSite/home.html',
                  {'link': 1, 'extUser': extUser, 'blogs': blogs, 'projects': projects,'socials':socials, })


def showBlogs(request):
    blogs = Blog.objects.filter(activeBlog=True)
    return render(request, 'JohnWebSite/blogs.html', {'link': 2, 'blogs': blogs,'socials':socials, })


def showWorks(request):
    projects = Project.objects.filter(activeProject=True)
    return render(request, 'JohnWebSite/works.html', {'link': 3, 'projects': projects,'socials':socials, })
