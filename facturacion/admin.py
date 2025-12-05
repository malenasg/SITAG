from django.contrib import admin
from .models import Factura, Pago, Presupuesto

class FacturaAdmin(admin.ModelAdmin):
    readonly_fields = ['monto_pagado']  # campo existente
    list_display = ['id', 'cliente', 'trabajo', 'monto_total', 'monto_pagado', 'estado', 'fecha_creacion']
    list_filter = ['estado', 'fecha_creacion']
    search_fields = ['cliente__nombre', 'trabajo__titulo']  # ajustá según tus campos de Cliente y Trabajo

admin.site.register(Factura, FacturaAdmin)

class PagoAdmin(admin.ModelAdmin):
    list_display = ['factura', 'trabajo_factura', 'monto', 'fecha']
    search_fields = ['factura__cliente__nombre', 'factura__trabajo__titulo']

    def trabajo_factura(self, obj):
        return obj.factura.trabajo
    trabajo_factura.short_description = "Trabajo"

admin.site.register(Pago, PagoAdmin)

class PresupuestoAdmin(admin.ModelAdmin):
    list_display = ['id', 'cliente', 'titulo', 'superficie', 'tipo', 'costo_estimado', 'aprobado', 'fecha']
    list_filter = ['aprobado', 'tipo', 'fecha']
    search_fields = ['cliente__nombre', 'titulo', 'ubicacion']

admin.site.register(Presupuesto, PresupuestoAdmin)
