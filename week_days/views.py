from django.shortcuts import render
from django.http import HttpResponse
from dataclasses import dataclass

# Create your views here.
@dataclass
class Days:
    day_name: str
    day_number: int
    description: str

monday = Days('monday', 1, 'список дел на понедельник')
tuesday= Days('tuesday', 2, 'список дел на вторник')
wednesday= Days('wednesday', 3, 'че там на среду')
thursday= Days('thursday', 4, 'че там на четверг')
friday = Days('friday', 5, 'Пятница на')
saturday= Days('saturday', 6, 'суббота же ж')
sunday= Days('sunday', 7, 'завтра на работу на')

days_list = [
    monday, tuesday, wednesday, thursday, friday, saturday, sunday
]



def get_info_about_day_of_week(request, day_of_week):
    res = ''
    for i in days_list:
        if i.day_name == day_of_week or i.day_number == day_of_week:
            res += i.description
            if res:
                return HttpResponse(res)
            else:
                return HttpResponse(f'нету такого дня- {day_of_week}')


# def get_info_about_day_of_week_as_number(request, day_of_week):
#     if day_of_week in days_list:
#         return HttpResponse(f'This is {day_of_week} day of weak')
#     else:
#         return HttpResponse(f'Неверный номер дня- {day_of_week}')

def index(request):
    li_elements = ''
    for i in days_list:
        li_elements += f"<li><a href= '{i.day_name}'>{i.day_name}</a></li>"
    response = f'''
        <ul>
        {li_elements}
        </ul>
        '''
    data = {
        'response' : response,
    }
    return render(request, 'week_days/greeting.html', context=data)
