from django.urls import path
from . import views

app_name = 'facturacion'

urlpatterns = [
    # Facturas
    path('', views.lista_facturas, name='lista_facturas'),
    path('nueva/', views.nueva_factura, name='nueva_factura'),
    path('editar/<int:factura_id>/', views.editar_factura, name='editar_factura'),

    # Pagos
    path('pago/nuevo/', views.nuevo_pago, name='nuevo_pago'),

    # Presupuestos
    path('presupuestos/', views.lista_presupuestos, name='lista_presupuestos'),
    path('presupuesto/nuevo/', views.nuevo_presupuesto, name='nuevo_presupuesto'),
]
