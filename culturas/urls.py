# culturas/urls.py
from django.urls import path, include
from .views import add_plantacao_view, plantacoes_info, weather_view

urlpatterns = [
    path('add/', add_plantacao_view, name='add_plantacao'),
    path('info/', plantacoes_info, name='plantacoes_info'),
    path('weather/', weather_view, name='weather'),
]
