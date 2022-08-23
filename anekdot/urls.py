from django.urls import path
from anekdot.views import showAnekdot

urlpatterns = [
    path('', showAnekdot, name='index'),
]
