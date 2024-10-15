from django.http import HttpResponseRedirect
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

from websitescraper_app.models import Links


def home(request):
    if request.method == "POST":
        link_new = request.POST.get('page', '')
        urls = requests.get("https://www.google.com/")
        beautysoup = BeautifulSoup(urls.text, 'html.parser')

        for links in beautysoup.find_all('a'):
            li_address = links.get('href')
            li_name = links.string
            links.objects.create(address=li_address, StringName=li_name)

        return HttpResponseRedirect('/')
    else:
        data_values = Links .objects.all()
    return render(request, 'home.html', {'data_values': data_values})
