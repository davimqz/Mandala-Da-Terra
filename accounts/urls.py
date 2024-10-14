from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView, name='home'),
    path('registro/', views.RegistroView, name='registro'),
    path('login/', views.LoginView, name='login'),
]

