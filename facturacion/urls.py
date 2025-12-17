from django.urls import path
from . import views

app_name = 'facturacion'

urlpatterns = [
    # **Presupuestos**
    path('presupuestos/', views.lista_presupuestos, name='lista_presupuestos'),
    path('presupuesto/nuevo/<int:trabajo_id>/', views.nuevo_presupuesto, name='nuevo_presupuesto'),
    path('presupuesto/<int:pk>/', views.detalle_presupuesto, name='detalle_presupuesto'),
    path('presupuesto/<int:pk>/cambiar-estado/', views.cambiar_estado_presupuesto, name='cambiar_estado_presupuesto'),
    
    # **Facturas**
    path('facturas/', views.lista_facturas, name='lista_facturas'),
    path('factura/<int:pk>/', views.detalle_factura, name='detalle_factura'),
    path('factura/<int:factura_id>/pago/', views.registrar_pago, name='registrar_pago'),
    path('factura/<int:pk>/pdf/', views.factura_pdf, name='factura_pdf'),

]
