from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.HomeView, name='home'),
    path('info_lavouras/', views.LavourasView, name='info_lavouras')
]

