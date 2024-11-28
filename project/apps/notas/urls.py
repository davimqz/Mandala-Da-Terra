from django.urls import path
# from .views import views_lista_notas, views_nova_nota, views_editar_nota, views_deletar_nota, views_confirmar_deletar, views_notificacao, views_meu_perfil, views_ver_nota
from .views import views_meu_perfil, views_notificacao
from . import views

app_name = 'notas'

urlpatterns = [
    path('meu_perfil/', views_meu_perfil, name='meu_perfil'),
    path('notificacao/', views_notificacao, name='notificacao'),
    path('anotar/', views.anotar, name='anotar'),
    path('editar/<int:id>/', views.editar_nota, name='editar_nota'),  
    path('remover/<int:id>/', views.remover_nota, name='remover_nota'),  
]
