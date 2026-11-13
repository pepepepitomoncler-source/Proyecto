from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
    # UD3.4.d - Nombre que se muestra en el administrador
    verbose_name = 'Entrenamientos'