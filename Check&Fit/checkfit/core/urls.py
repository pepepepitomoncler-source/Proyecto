# UD3.7.b
from django.urls import path
from . import views

urlpatterns = [
    path('usuario_list/', views.UsuarioListView.as_view(), name='usuario_list'),
    path('usuario_detail/<int:pk>/', views.UsuarioDetailView.as_view(), name='usuario_detail'),
    path('entrenador_list/', views.EntrenadorListView.as_view(), name='entrenador_list'),
    path('entrenador_detail/<int:pk>/', views.EntrenadorDetailView.as_view(), name='entrenador_detail'),
    path('rutina_list/', views.RutinaListView.as_view(), name='rutina_list'),
    path('rutina_detail/<int:pk>/', views.RutinaDetailView.as_view(), name='rutina_detail'),
    path('ejercicio_list/', views.EjercicioListView.as_view(), name='ejercicio_list'),
    path('ejercicio_detail/<int:pk>/', views.EjercicioDetailView.as_view(), name='ejercicio_detail'),
    path('registroentreno_list/', views.RegistroEntrenoListView.as_view(), name='registroentreno_list'),
    path('registroentreno_detail/<int:pk>/', views.RegistroEntrenoDetailView.as_view(), name='registroentreno_detail'),
]