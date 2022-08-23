from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from JohnWebSite.models import Social

def showAnekdot(request):
    socials = Social.objects.all()
    response = requests.get('https://www.anekdot.ru/')
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all(class_='text')
    anekdots = []
    for quote in quotes:
        anekdots.append(quote.text)

    return render(request, 'anekdot/anekdot.html', {'link': 4,'anekdots': anekdots, 'socials': socials,})
   