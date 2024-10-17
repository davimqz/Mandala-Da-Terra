from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views  # Importar views de autenticação



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('contas.urls')),
    path('culturas/', include('culturas.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Adicione esta linha
    
]
