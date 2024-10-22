from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views  # Importar views de autenticação
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.contas.urls')),
    path('culturas/', include('apps.culturas.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Adicione esta linha
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)