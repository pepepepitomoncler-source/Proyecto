# UD3.6.a
from decimal import Decimal
from datetime import date, timedelta

from django.db.models import F

from billing.models import Cliente, Factura, Cobro


# UD3.6.a - 1. Todos los clientes
def get_clientes_all():
    return Cliente.objects.all()


# UD3.6.a - 2. Las 3 primeras facturas
def get_factura_first_3():
    return Factura.objects.all()[:3]


# UD3.6.a - 3. Facturas de importe 0
def get_factura_0():
    return Factura.objects.filter(total=0)


# UD3.6.a - 4. Clientes cuyo DNI no empieza por "74"
def get_cliente_not_0612():
    return Cliente.objects.exclude(nif__startswith='74')


# UD3.6.a - 5. Clientes con DNI '92436593F' y apellidos que contienen "Pérez"
def get_cliente_dni_apellido():
    return Cliente.objects.filter(nif='92436593F', apellidos__contains='Pérez')


# UD3.6.a - 6. Facturas con id menor a 2, ordenadas por número de factura descendente
def get_cli_id_lt_2_num_fact_des():
    return Factura.objects.filter(id__lt=2).order_by('-numero_factura')


# UD3.6.a - 7. Clientes con id mayor a 2
def get_cli_id_gt_2():
    return Cliente.objects.filter(id__gt=2)


# UD3.6.a - 8. Facturas con "PHP" en el concepto, ordenadas por número de factura ascendente
def get_fact_des_nom_des():
    return Factura.objects.filter(concepto__contains='PHP').order_by('numero_factura')


# UD3.6.a - 9. Facturas cuyo número no acaba en "1"
def get_fact_not_1():
    return Factura.objects.exclude(numero_factura__endswith='1')


# UD3.6.a - 10. Primer cobro (objeto) cuya factura contiene "python" y cuyo id acaba en "2"
def get_cobro_python_id2():
    return Cobro.objects.filter(factura__concepto__icontains='python', id__endswith='2').first()


# UD3.6.a - 11. Cobros de facturas con "06" en el número, excluyendo clientes con "Manu" en el nombre
def get_cobro_fact6_not_manu():
    return Cobro.objects.filter(factura__numero_factura__contains='06').exclude(factura__cliente__nombre__contains='Manu')


# UD3.6.a - 12. Facturas con importe mayor o igual a 5
def get_fact_gt_5():
    return Factura.objects.filter(total__gte=5)


# UD3.6.a - 13. Cobros con importe entre 5 y 10
def get_cobro_5_10():
    return Cobro.objects.filter(importe__range=(5, 10))


# UD3.6.a - 14. Crear el cliente "Nuevo apellido1 apellido2" con un DNI válido
def create_cliente():
    cliente, creado = Cliente.objects.get_or_create(
        nif='12345678Z',
        defaults={'nombre': 'Nuevo', 'apellidos': 'apellido1 apellido2', 'email': 'nuevo@example.com'},
    )
    return cliente


# UD3.6.a - 15. Crear una factura para el cliente anterior, con fecha de ayer e importe 100
def create_factura():
    factura, creada = Factura.objects.get_or_create(
        numero_factura='F-NUEVA-100',
        defaults={
            'cliente': create_cliente(),
            'concepto': 'Factura de prueba creada con el ORM',
            'fecha': date.today() - timedelta(days=1),
            'total': Decimal('100'),
        },
    )
    return factura


# UD3.6.a - 16. Añadir "(última)" al concepto de la última factura
def update_last_factura():
    factura = Factura.objects.order_by('id').last()
    factura.concepto = factura.concepto + ' (última)'
    factura.save()
    return factura


# UD3.6.a - 17. Multiplicar por 2 el importe de los cobros de facturas cuyo número acaba en "2"
def update_cobro_fact2_x2():
    return Cobro.objects.filter(factura__numero_factura__endswith='2').update(importe=F('importe') * 2)


# UD3.6.a - 18. Dividir entre 2 el importe de los cobros de facturas acabadas en "1" de clientes con "González"
def update_cobro_fact1_cligonz_div2():
    return Cobro.objects.filter(
        factura__numero_factura__endswith='1',
        factura__cliente__apellidos__contains='González',
    ).update(importe=F('importe') / 2)


# UD3.6.a - 19. Eliminar los cobros cuyas facturas tengan un importe menor a 1
def delete_cobro_fact_lt_1():
    return Cobro.objects.filter(factura__total__lt=1).delete()


# UD3.6.a - 20. Eliminar los cobros de facturas cuyo cliente contiene "Pablo" en el nombre
def delete_cobro_cli_pablo():
    return Cobro.objects.filter(factura__cliente__nombre__contains='Pablo').delete()