# culturas/urls.py
from django.urls import path, include
from .views import add_plantacao_view, plantacoes_info

urlpatterns = [
    path('add/', add_plantacao_view, name='add_plantacao'),
    path('info/', plantacoes_info, name='plantacoes_info'),

]
