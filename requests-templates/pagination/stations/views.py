from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv

from pagination.settings import BASE_DIR


def index(request):
    return redirect(reverse('bus_stations'))


def get_list_stations():
    stations = []
    with open(str(BASE_DIR) +'/data-398-2018-08-30.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for line in reader:
            stations.append({'Name': line['StationName'], 'Street': line['Street'], 'District': line['District']})
    return stations


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    list_stations = get_list_stations()
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(list_stations, 10)
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': page.object_list,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
