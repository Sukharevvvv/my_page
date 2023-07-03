from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def index(request):
    data = {
        'city_born' : 'Вольск',
        'movie_name' : 'Бригада',
        'year_born' : 1977,
    }
    return render(request, 'cinema/cinema.html', context=data)

def hinnes(request):
    data = {
        'power_man' : 'Narve Laeret',
        'bar_name' : 'Bob`s BBQ & Grill',
        'count_needle' : 1790,
    }
    return render(request, 'cinema/hinnes.html', context=data)