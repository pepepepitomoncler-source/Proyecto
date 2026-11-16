# UD3.4.c - Administrador de la app core
from django.contrib import admin
from .models import Usuario, Entrenador, Rutina, Ejercicio, RegistroEntreno


# UD3.4.c
class UsuarioAdmin(admin.ModelAdmin):
    list_display = list_display_links = ('nombre', 'email', 'rol', 'fecha_registro')  # columnas y enlaces de la lista
    list_filter = ('rol',)  # filtro lateral por rol
    search_fields = ('nombre', 'email')  # campos donde busca el buscador
    preserve_filters = True  # mantiene los filtros al volver de editar


# UD3.4.c
class EntrenadorAdmin(admin.ModelAdmin):
    list_display = list_display_links = ('usuario', 'especialidad', 'experiencia')
    list_filter = ('especialidad',)
    search_fields = ('usuario__nombre', 'especialidad')
    preserve_filters = True


# UD3.4.c
class RutinaAdmin(admin.ModelAdmin):
    list_display = list_display_links = ('nombre', 'cliente', 'entrenador', 'fecha_creacion')
    list_filter = ('entrenador',)
    search_fields = ('nombre', 'cliente__nombre')
    preserve_filters = True


# UD3.4.c
class EjercicioAdmin(admin.ModelAdmin):
    list_display = list_display_links = ('nombre', 'rutina', 'series', 'repeticiones', 'peso_recomendado')
    list_filter = ('rutina',)
    search_fields = ('nombre', 'rutina__nombre')
    preserve_filters = True


# UD3.4.c
class RegistroEntrenoAdmin(admin.ModelAdmin):
    list_display = list_display_links = ('cliente', 'ejercicio', 'peso_levantado', 'repeticiones', 'fecha')
    list_filter = ('cliente',)
    search_fields = ('cliente__nombre', 'ejercicio__nombre')
    preserve_filters = True


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Entrenador, EntrenadorAdmin)
admin.site.register(Rutina, RutinaAdmin)
admin.site.register(Ejercicio, EjercicioAdmin)
admin.site.register(RegistroEntreno, RegistroEntrenoAdmin)