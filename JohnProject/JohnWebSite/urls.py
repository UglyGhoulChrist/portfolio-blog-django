from django.urls import path
from JohnWebSite.views import showHome, showBlogs, showWorks

urlpatterns = [
    path('', showHome, name='home'),
    path('blogs/', showBlogs, name='blogs'),
    path('works/', showWorks, name='works'),
]
