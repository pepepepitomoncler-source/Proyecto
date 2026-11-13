# UD3.7.b
from django.urls import path
from . import views

urlpatterns = [
    path('cliente_list/', views.ClienteListView.as_view(), name='cliente_list'),
    path('cliente_detail/<int:pk>/', views.ClienteDetailView.as_view(), name='cliente_detail'),
    path('factura_list/', views.FacturaListView.as_view(), name='factura_list'),
    path('factura_detail/<int:pk>/', views.FacturaDetailView.as_view(), name='factura_detail'),
    path('cobro_list/', views.CobroListView.as_view(), name='cobro_list'),
    path('cobro_detail/<int:pk>/', views.CobroDetailView.as_view(), name='cobro_detail'),
]