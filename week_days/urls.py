from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<day_of_week>/', views.get_info_about_day_of_week),
]

