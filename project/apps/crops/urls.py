from django.urls import path
from . import views

app_name = "crops"

urlpatterns = [
    path('praga/', views.pragas, name='praga'),
    path('tasks/', views.task_list, name='task_list'),
    path('task/new/', views.task_create, name='task_create'),
    path('task/<int:pk>/edit/', views.task_edit, name='task_edit'),
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('home/', views.home_view, name='home'),   
    
    path('caramujo/', views.caramujo, name='caramujo'),
    path('lagarta/', views.lagarta, name='lagarta'),
    path('tomate/', views.tomate, name='tomate'),
    
    path('pesquisar/', views.pesquisar_cultura, name='pesquisar_cultura'),
    path('cultura/<int:cultura_id>/', views.detalhes_cultura, name='detalhes_cultura'),

]

