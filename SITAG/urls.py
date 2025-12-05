from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def home_redirect(request):
    if request.user.is_authenticated:
        return redirect('inicio:inicio')
    else:
       return redirect('usuarios:login')

urlpatterns = [
    path('admin/', admin.site.urls),

    # raíz redirige automáticamente
    path('', home_redirect, name='home'),

    # apps
    path('inicio/', include(('inicio.urls', 'inicio'), namespace='inicio')),
    path('clientes/', include(('clientes.urls', 'clientes'), namespace='clientes')),
    path('trabajos/', include(('trabajos.urls', 'trabajos'), namespace='trabajos')),
    path('usuarios/', include(('usuarios.urls', 'usuarios'), namespace='usuarios')),
    path('facturacion/', include(('facturacion.urls', 'facturacion'), namespace='facturacion')),

]


