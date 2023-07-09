from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

zodiac_dict = {
    'aries' : ['Овен супер четкий знак', 'fire'],
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
        data = {
            "description" : description[0],
            "current_sign" : sign_zodiac,
        }
        return render(request, 'horoscope/info_zodiac.html',  context=data)
    else:
        return HttpResponseNotFound('шо за дела')

def get_info_about_zodiac_sign_by_number(request, sign_zodiac:int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(f'Неправильный порядковый номер зодиака {sign_zodiac}')
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_url = reverse('horoscope_name', args=(name_zodiac, ))
    return HttpResponseRedirect(redirect_url)

def index(request):
    zodiacs = list(zodiac_dict)
    data = {
        'zodiacs' : zodiacs
    }
    return render(request, 'horoscope/index.html', context=data)

def element_types(request):
    zodiac_list = list(zodiac_dict.values())
    res = []
    for sub_list in zodiac_list:
        res.append(sub_list[1])
    res = list(set(res))
    li_elements = ''
    for element in res:
        li_elements += f"<li><a href= '{element}'>{element.title()}</a></li>"
    response = f'''
    <ul>
    {li_elements}
    </ul>
    '''
    return HttpResponse(response)

def element(request, changed_element):
  res = []
  for el in zodiac_dict:
    if changed_element == (zodiac_dict[el])[1]:
      res.append(el)
    else:
        continue
  if res:
    li_elements = ''
    for element in res:
        redirect_path = reverse('horoscope_name', args=[element])
        li_elements += f"<li><a href= '{redirect_path}'>{element.title()}</a></li>"
        response = f'''
            <ul>
            {li_elements}
            </ul>
            '''
    return HttpResponse(response)
  else:
      return HttpResponseNotFound(f'Нету такой стихии в международной космоэнергетике- {changed_element}')
