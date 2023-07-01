from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

zodiac_dict = {
    'aries' : ['Овен', 'fire'],
    'taurus' : ['Телец на', 'earth'],
    'gemini': ['Близняшки няшки', 'air'],
    'cancer': ['Раааак- отличный самый знак. И весы хотят полтора килограмма колбасы.', 'water'],
    'leo': ['Львенок, как теленок', 'fire'],
    'virgo': ['Девица как знак', 'earth'],
    'libra': ['Следи за весом, весы- знак', 'air'],
    'scorpio': ['Скорпион- круче Саб-Зиро', 'water'],
    'sagittarius': ['Стрелец- молодец', 'fire'],
    'capricorn': ['Козегог рок рок', 'earth'],
    'aquarius': ['Водолей лей- лей', 'air'],
    'pisces': ['Рыбы бы бы бы', 'water'],
}
def get_info_about_zodiac_sign(request, sign_zodiac):
    description = zodiac_dict.get(sign_zodiac, None)
    if description:
        return HttpResponse(description[0])
    else:
        return HttpResponseNotFound(f'Нету такого знака зодиака- {sign_zodiac}')

def get_info_about_zodiac_sign_by_number(request, sign_zodiac:int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(f'Неправильный порядковый номер зодивка {sign_zodiac}')
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_url = reverse('horoscope_name', args=(name_zodiac, ))
    return HttpResponseRedirect(redirect_url)

def index(request):
    zodiacs = list(zodiac_dict)
    li_elements = ''
    for sign in zodiacs:
        redirect_path = reverse('horoscope_name', args=[sign])
        li_elements += f"<li><a href= '{redirect_path}'>{sign.title()}</a></li>"
    response = f'''
    <ol>
    {li_elements}
    </ol>
    '''
    return HttpResponse(response)

def element_types(request):
    zodiac_list = list(zodiac_dict.values())
    res = []
    for sub_list in zodiac_list:
        res.append(sub_list[1])
    res = list(set(res))
    li_elements = ''
    for element in res:
        redirect_path = reverse('element_type')
        li_elements += f"<li><a href= '{element}'>{element}</a></li>"
    response = f'''
    <ol>
    {li_elements}
    </ol>
    <br>
    <h1>Слава, я заморочился и создал роут на фиг и представление к нему, а роут настолько динамический,
     что ненумерованный список формируется на основании значений вложенного списка атрибутов 
     знаков зодиака<h1>
    '''
    return HttpResponse(response)
