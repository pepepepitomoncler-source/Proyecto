# UD3.7.a - Vistas de la app core (Anexo III, Tabla 1)
from django.views.generic import ListView, DetailView
from .models import Usuario, Entrenador, Rutina, Ejercicio, RegistroEntreno


# UD3.7.a
class UsuarioListView(ListView):
    model = Usuario
    template_name = 'core/usuario_list.html'
    paginate_by = 5  # UD3.8.b


# UD3.7.a
class UsuarioDetailView(DetailView):
    model = Usuario
    template_name = 'core/usuario_detail.html'


# UD3.7.a
class EntrenadorListView(ListView):
    model = Entrenador
    template_name = 'core/entrenador_list.html'
    paginate_by = 5  # UD3.8.b


# UD3.7.a
class EntrenadorDetailView(DetailView):
    model = Entrenador
    template_name = 'core/entrenador_detail.html'


# UD3.7.a
class RutinaListView(ListView):
    model = Rutina
    template_name = 'core/rutina_list.html'
    paginate_by = 5  # UD3.8.b


# UD3.7.a
class RutinaDetailView(DetailView):
    model = Rutina
    template_name = 'core/rutina_detail.html'


# UD3.7.a
class EjercicioListView(ListView):
    model = Ejercicio
    template_name = 'core/ejercicio_list.html'
    paginate_by = 5  # UD3.8.b


# UD3.7.a
class EjercicioDetailView(DetailView):
    model = Ejercicio
    template_name = 'core/ejercicio_detail.html'


# UD3.7.a
class RegistroEntrenoListView(ListView):
    model = RegistroEntreno
    template_name = 'core/registroentreno_list.html'
    paginate_by = 5  # UD3.8.b


# UD3.7.a
class RegistroEntrenoDetailView(DetailView):
    model = RegistroEntreno
    template_name = 'core/registroentreno_detail.html'