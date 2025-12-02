from django.contrib import admin
from .models import Factura, ProductoFactura
from .models import SemanaHistorial



class ProductoFacturaInline(admin.TabularInline):
    model = ProductoFactura
    extra = 1


@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ('numero_factura', 'proveedor', 'fecha')
    inlines = [ProductoFacturaInline]


@admin.register(ProductoFactura)
class ProductoFacturaAdmin(admin.ModelAdmin):
    list_display = ('nombre_producto', 'factura', 'precio')


admin.site.register(SemanaHistorial)