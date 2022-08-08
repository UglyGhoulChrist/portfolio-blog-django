from django.contrib import admin
from .models import ExtUser, Social, Blog,Project


@admin.register(ExtUser)
class ExtUserAdmin(admin.ModelAdmin):
    list_display = ['helloExtUser', 'descriptionExtUser']


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ['titleSocial',  'linkSocial']


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['titleBlog',  'activeBlog' ,'createdBlog','linkBlog']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['titleProject', 'activeProject','createdProject', 'linkProject']    