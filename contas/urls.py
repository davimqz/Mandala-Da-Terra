from django.urls import path
from . import views
from culturas.views import saf_view, horta_view, add_plantacao_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),  
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('saf/', views.saf_view, name='saf'),
    path('horta/', views.horta_view, name='horta'),
    path('app_plantacao/', views.add_plantacao_view, name='add_plantacao'),
    path('painel/', views.painel_view, name='painel'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)