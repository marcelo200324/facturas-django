from django.db import models


class Factura(models.Model):
    fecha = models.DateField()
    proveedor = models.CharField(max_length=200)
    numero_factura = models.CharField(max_length=50, unique=True)
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"Factura {self.numero_factura} - {self.proveedor}"

    @property
    def total(self):
        return sum(item.precio for item in self.productos.all())


class ProductoFactura(models.Model):
    factura = models.ForeignKey(
        Factura,
        related_name='productos',
        on_delete=models.CASCADE
    )
    nombre_producto = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nombre_producto} ({self.factura.numero_factura})"


class SemanaHistorial(models.Model):
    inicio_semana = models.DateField()
    fin_semana = models.DateField()
    total_semana = models.DecimalField(max_digits=12, decimal_places=0)

    def __str__(self):
        return f"Semana {self.inicio_semana} a {self.fin_semana} - Total: {self.total_semana}"
