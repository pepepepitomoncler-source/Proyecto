from django.db import models
from django.utils import timezone


# UD3.3.a
class Cliente(models.Model):
    nombre = models.CharField(max_length=256, verbose_name='Nombre')
    apellidos = models.CharField(max_length=512, verbose_name='Apellidos')
    nif = models.CharField(max_length=20, unique=True, verbose_name='NIF')
    email = models.EmailField(unique=True, verbose_name='Email')

    class Meta:
        # UD3.3.c
        unique_together = (('nif',), ('email',))
        # UD3.4.e
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        # UD3.4.f
        ordering = ['apellidos', 'nombre']

    # UD3.3.b
    def __str__(self):
        return self.nombre + ' ' + self.apellidos + ' (' + self.nif + ')'

# UD3.3.a
class Factura(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, verbose_name='Cliente')
    numero_factura = models.CharField(max_length=20, verbose_name='N.º factura')
    concepto = models.TextField(verbose_name='Concepto')
    fecha = models.DateField(default=timezone.localdate, verbose_name='Fecha')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Total')

    class Meta:
        # UD3.3.c
        unique_together = (('numero_factura',),)
        # UD3.4.e
        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'
        # UD3.4.f
        ordering = ['numero_factura']

    # UD3.3.b
    def __str__(self):
        return str(self.cliente) + ' - ' + self.numero_factura


# UD3.3.a
class Cobro(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.PROTECT, verbose_name='Factura')
    fecha = models.DateField(default=timezone.localdate, verbose_name='Fecha')
    importe = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Importe')

    class Meta:
        # UD3.4.e
        verbose_name = 'Cobro'
        verbose_name_plural = 'Cobros'
        # UD3.4.f
        ordering = ['-fecha']

    # UD3.3.b
    def __str__(self):
        return self.factura.numero_factura + ' - ' + str(self.importe)