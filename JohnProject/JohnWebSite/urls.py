from django.urls import path
from JohnWebSite.views import index 

urlpatterns = [
    path('', index),
]
