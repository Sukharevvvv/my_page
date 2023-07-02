from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:day_of_week>/', views.get_info_about_day_of_week_as_number),
    path('<str:day_of_week>/', views.get_info_about_day_of_week),
]

