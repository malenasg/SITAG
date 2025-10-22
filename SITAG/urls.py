from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inicio.urls')),
    path('clientes/', include(('clientes.urls', 'clientes'), namespace='clientes')),
    path('trabajos/', include(('trabajos.urls', 'trabajos'), namespace='trabajos')),
    path('usuarios/', include('usuarios.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
