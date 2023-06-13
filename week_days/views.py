from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

days_dict = {
    'monday': 'список дел на понедельник',
    'tuesday': 'список дел на вторник',
}


def get_info_about_day_of_week(request, day_of_week):
    description = days_dict.get(day_of_week)
    if description:
        return HttpResponse(description)
    else:
        return HttpResponse(f'нету такого дня- {day_of_week}')

days_list = [1, 2 ,3 , 4, 5 , 6, 7,]
def get_info_about_day_of_week_as_number(request, day_of_week):
    if day_of_week in days_list:
        return HttpResponse(f'This is {day_of_week} day of weak')
    else:
        return HttpResponse(f'Неверный номер дня- {day_of_week}')