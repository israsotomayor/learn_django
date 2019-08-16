from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_list, name='car_list')
]