from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.contas.urls')),
    path('plantacoes/', include('apps.plantacoes.urls')),
]
