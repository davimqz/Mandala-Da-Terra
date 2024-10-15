from django.urls import path
from . import views

urlpatterns = [
   path('home/', views.HomeView, name='home'),
   path('saf/', views.SafView, name='saf'),
   path('horta/', views.HortaView, name='horta'),
   path('adicionar_plantacao', views.AdicionarPlantacaoView, name='adicionar_plantacao')
]
