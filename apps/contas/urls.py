from django.urls import path
from . import views

urlpatterns = [
   path('', views.RegistroView, name='registro'),
   path('login/', views.LoginView, name='login'),
   path('cadastro/', views.CadastroView, name='cadastro'),
]
