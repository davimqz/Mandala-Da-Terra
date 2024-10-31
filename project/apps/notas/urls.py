from django.urls import path
from .views import views_lista_notas, views_nova_nota, views_editar_nota, views_deletar_nota, views_confirmar_deletar, views_notificacao, views_meu_perfil, views_ver_nota

app_name = 'notas'

urlpatterns = [
    path('lista_notas/', views_lista_notas, name='lista_notas'),
    path('nova/', views_nova_nota, name='nova_nota'),
    path('editar/<int:id>/', views_editar_nota, name='editar_nota'),
    path('deletar/<int:id>/', views_deletar_nota, name='deletar_nota'),
    path('confirmar_deletar/<int:nota_id>/', views_confirmar_deletar, name='confirmar_deletar'),
    path('meu_perfil/', views_meu_perfil, name='meu_perfil'),
    path('notificacao/', views_notificacao, name='notificacao'),\
    path('<int:nota_id>/ver/', views_ver_nota, name='ver_nota'),


]
