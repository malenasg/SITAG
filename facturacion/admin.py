from django.contrib import admin
from .models import Factura, Presupuesto

@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente_nombre', 'presupuesto', 'fecha', 'monto_pagado', 'pagada')
    readonly_fields = ('fecha', 'monto_pagado')
    list_filter = ('pagada', 'fecha')
    search_fields = ('presupuesto__cliente__nombre',)

    def cliente_nombre(self, obj):
        return obj.presupuesto.cliente
    cliente_nombre.short_description = "Cliente"


@admin.register(Presupuesto)
class PresupuestoAdmin(admin.ModelAdmin):
    list_display = ("id", "get_cliente", "estado")
    list_filter = ('estado', 'fecha')
    search_fields = ('trabajo__cliente__nombre', 'trabajo__titulo')

    def get_cliente(self, obj):
        return obj.trabajo.cliente.nombre
    get_cliente.short_description = "Cliente"
