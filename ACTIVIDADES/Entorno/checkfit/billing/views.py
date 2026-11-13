from django.shortcuts import render
from django.views.generic import ListView, DetailView
from billing.models import Cliente, Factura, Cobro
from .models import Cliente, Factura, Cobro
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# UD4.2a
class ClienteListView(ListView):
    model = Cliente
    template_name = 'billing/cliente_list.html'

# UD4.2a
class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'billing/cliente_detail.html'

# UD4.2a
class FacturaListView(ListView):
    model = Factura
    template_name = 'billing/factura_list.html'

# UD4.2a
class FacturaDetailView(DetailView):
    model = Factura
    template_name = 'billing/factura_detail.html'

# UD4.2a
class CobroListView(ListView):
    model = Cobro
    template_name = 'billing/cobro_list.html'

# UD4.2a
class CobroDetailView(DetailView):
    model = Cobro
    template_name = 'billing/cobro_detail.html'

# UD4.2a
class ClienteCreateView(CreateView):
    model = Cliente
    template_name = '/billing/base_create_udpate.html'
    success_url = reverse_lazy('cliente_update')

# UD4.2a
class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = '/billing/base_create_udpate.html'
    success_url = reverse_lazy('cliente_update')

# UD4.2a
class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'billing/base_create_delete.html'
    success_url = reverse_lazy('cliente_list')
    
# UD4.2a
class FacturaCreateView(CreateView):
    model = Factura
    template_name = '/billing/base_create_udpate.html'
    success_url = reverse_lazy('factura_update')

# UD4.2a
class FacturaUpdateView(UpdateView):
    model = Factura
    template_name = '/billing/base_create_udpate.html'
    success_url = reverse_lazy('factura_update')

# UD4.2a
class FacturaDeleteView(DeleteView):
    model = Factura 
    template_name = '/billing/base_confirm_delete.html'
    success_url = reverse_lazy('factura_list')

# UD4.2a
class CobroCreateView(CreateView):
    model = Cobro
    template_name = 'billing/base_create_udpate.html'
    success_url = reverse_lazy('cobro_update')

# UD4.2a
class CobroUpdateView(UpdateView):
    model = Cobro
    template_name = 'billing/base_create_udpate.html'
    success_url = reverse_lazy('cobro_update')

# UD4.2a
class CobroDeleteView(DeleteView):
    model = Cobro
    template_name = 'billing/base_confirm_delete.html'
    success_url = reverse_lazy('cobro_list')

