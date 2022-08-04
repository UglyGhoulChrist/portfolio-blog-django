from django.urls import path
from JohnWebSite.views import home , blogs , works

urlpatterns = [
    path('', home, name='home'),
    path('blogs/', blogs, name='blogs'),
    path('works/', works, name='works'),
]
