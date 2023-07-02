from django.urls import path
from . import views

urlpatterns = [
    path('type/<changed_element>/', views.element, name='element'),
    path('type/', views.element_types, name='element_type'),
    path('', views.index),
    path('<int:sign_zodiac>/', views.get_info_about_zodiac_sign_by_number),
    path('<str:sign_zodiac>/', views.get_info_about_zodiac_sign, name='horoscope_name'),
]
