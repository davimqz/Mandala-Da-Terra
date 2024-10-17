# culturas/urls.py
from django.urls import path
from .views import add_plantacao_view, plantacoes_info

urlpatterns = [
    path('add/', add_plantacao_view, name='add_plantacao'),
    path('plantacoes_info/<str:nome>/', plantacoes_info, name='plantacoes_info'),

]
