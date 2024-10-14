from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    # path('registro/', views.RegistroView, name='registro'),
    path('login/', views.login_view, name='login'),  
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('logout/', views.logout, name='logout'),
]
