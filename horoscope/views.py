from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

zodiac_dict = {
    'aries' : 'Овен',
    'taurus' : 'Телец на',
    'gemini': 'Близняшки няшки',
    'cancer': 'Раааак- отличный самый знак. И весы хотят полтора килограмма колбасы.',
    'leo': 'Львенок, как теленок',
    'virgo': 'Девица как знак',
    'libra': 'Следи за весом, весы- знак',
    'scorpio': 'Скорпион- круче Саб-Зиро',
    'sagittarius': 'Стрелец- молодец',
    'capricorn': 'Козегог рок рок',
    'aquarius': 'Водолей лей- лей',
    'pisces': 'Рыбы бы бы бы',
}

def get_info_about_zodiac_sign(request, sign_zodiac):
    description = zodiac_dict.get(sign_zodiac, None)
    if description:
        return HttpResponse(description)
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