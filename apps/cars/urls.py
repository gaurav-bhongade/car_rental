from django.urls import path
from . import views

urlpatterns = [
    path('', views.cars_list, name='cars_list'),
    path('<int:pk>/', views.car_detail, name='car_detail'),
]