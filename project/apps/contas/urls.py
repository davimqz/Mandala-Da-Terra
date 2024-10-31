from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),  
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('saf/', views.saf_view, name='saf'),
    path('horta/', views.horta_view, name='horta'),
] 


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)