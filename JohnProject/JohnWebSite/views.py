from django.shortcuts import render

def home(request):
    return render(request, 'JohnWebSite/home.html')

def blogs(request):
    return render(request, 'JohnWebSite/blogs.html')

def works(request):
    return render(request, 'JohnWebSite/works.html')