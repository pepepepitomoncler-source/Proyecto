from django.db import models
from django.utils.timezone import now


# UD3.3.a
class Usuario(models.Model):
    nombre = models.CharField(max_length=256, verbose_name='Nombre')
    email = models.EmailField(unique=True, verbose_name='Email')
    contrasena = models.CharField(max_length=128, verbose_name='Contraseña')
    rol = models.CharField(max_length=50, verbose_name='Rol')
    fecha_registro = models.DateTimeField(default=now, verbose_name='Fecha de registro')

    class Meta:
        # UD3.3.c 
        unique_together = (('email',),)
        # UD3.4.e
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        # UD3.4.f
        ordering = ['nombre']

    # UD3.3.b
    def __str__(self):
        return self.nombre + ' (' + self.email + ')'


# UD3.3.a
class Entrenador(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, verbose_name='Usuario')
    especialidad = models.CharField(max_length=256, verbose_name='Especialidad')
    experiencia = models.PositiveIntegerField(verbose_name='Años de experiencia')
    descripcion = models.TextField(verbose_name='Descripción')

    class Meta:
        # UD3.3.c
        unique_together = (('usuario',),)
        # UD3.4.e
        verbose_name = 'Entrenador'
        verbose_name_plural = 'Entrenadores'
        # UD3.4.f
        ordering = ['usuario__nombre']

    # UD3.3.b
    def __str__(self):
        return str(self.usuario) + ' - ' + self.especialidad


# UD3.3.a
class Rutina(models.Model):
    cliente = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name='rutinas', verbose_name='Cliente')
    entrenador = models.ForeignKey(Entrenador, on_delete=models.PROTECT, related_name='rutinas', verbose_name='Entrenador')
    nombre = models.CharField(max_length=256, verbose_name='Nombre')
    descripcion = models.TextField(verbose_name='Descripción')
    fecha_creacion = models.DateTimeField(default=now, verbose_name='Fecha de creación')

    class Meta:
        # UD3.3.c
        unique_together = (('cliente', 'nombre'),)
        # UD3.4.e
        verbose_name = 'Rutina'
        verbose_name_plural = 'Rutinas'
        # UD3.4.f
        ordering = ['-fecha_creacion']

    # UD3.3.b
    def __str__(self):
        return self.nombre + ' - ' + str(self.cliente)


# UD3.3.a
class Ejercicio(models.Model):
    rutina = models.ForeignKey(Rutina, on_delete=models.CASCADE, related_name='ejercicios', verbose_name='Rutina')
    nombre = models.CharField(max_length=256, verbose_name='Nombre')
    series = models.PositiveIntegerField(verbose_name='Series')
    repeticiones = models.PositiveIntegerField(verbose_name='Repeticiones')
    peso_recomendado = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Peso recomendado (kg)')

    class Meta:
        # UD3.3.c
        unique_together = (('rutina', 'nombre'),)
        # UD3.4.e
        verbose_name = 'Ejercicio'
        verbose_name_plural = 'Ejercicios'
        # UD3.4.f
        ordering = ['rutina__nombre', 'nombre']

    # UD3.3.b
    def __str__(self):
        return self.nombre + ' (' + self.rutina.nombre + ')'


# UD3.3.a
class RegistroEntreno(models.Model):
    cliente = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name='registros', verbose_name='Cliente')
    ejercicio = models.ForeignKey(Ejercicio, on_delete=models.PROTECT, related_name='registros', verbose_name='Ejercicio')
    peso_levantado = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Peso levantado (kg)')
    repeticiones = models.PositiveIntegerField(verbose_name='Repeticiones')
    fecha = models.DateTimeField(default=now, verbose_name='Fecha')

    class Meta:
        # UD3.3.c
        unique_together = (('cliente', 'ejercicio', 'fecha'),)
        # UD3.4.e
        verbose_name = 'Registro de entreno'
        verbose_name_plural = 'Registros de entreno'
        # UD3.4.f
        ordering = ['-fecha']

    # UD3.3.b
    def __str__(self):
        return self.cliente.nombre + ' - ' + self.ejercicio.nombre + ' - ' + self.fecha.strftime('%d/%m/%Y')