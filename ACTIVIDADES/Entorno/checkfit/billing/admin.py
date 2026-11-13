# UD3.4.b - Administrador de la app billing
from django.contrib import admin
from .models import Cliente, Factura, Cobro


# UD3.4.b
class ClienteAdmin(admin.ModelAdmin):
    # UD3.4.a
    list_display = list_display_links = ('nombre', 'apellidos', 'nif', 'email')  # columnas de la lista y enlaces al detalle
    list_filter = ('nif',)  # filtro lateral por NIF
    search_fields = ('nombre', 'apellidos', 'nif', 'email')  # campos donde busca el buscador
    preserve_filters = True  # mantiene los filtros al volver de editar un registro


# UD3.4.b - FacturaAdmin
class FacturaAdmin(admin.ModelAdmin):
    list_display = list_display_links = ('numero_factura', 'fecha', 'total')
    list_filter = ('cliente',)
    search_fields = ('numero_factura', 'cliente__nombre', 'cliente__apellidos')
    preserve_filters = True


# UD3.4.b - CobroAdmin
class CobroAdmin(admin.ModelAdmin):
    list_display = list_display_links = ('numero_factura', 'fecha', 'importe')
    list_filter = ('factura__cliente',)
    search_fields = ('factura__numero_factura', 'factura__cliente__nombre', 'factura__cliente__apellidos')
    preserve_filters = True

    @admin.display(description='N.º factura', ordering='factura__numero_factura')
    def numero_factura(self, obj):
        return obj.factura.numero_factura


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Factura, FacturaAdmin)
admin.site.register(Cobro, CobroAdmin)