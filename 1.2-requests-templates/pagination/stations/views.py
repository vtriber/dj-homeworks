import csv
from pprint import pprint

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    content = []
    with open('data-398-2018-08-30.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            station = {}
            station['Name'] = row['Name']
            station['Street'] = row['Street']
            station['District'] = row['District']
            content.append(station)
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(content, 10)
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
