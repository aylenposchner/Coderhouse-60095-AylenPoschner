from ..forms import TransaccionForm
from ..models import Transaccion
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy

class TransaccionListView(ListView):
    model = Transaccion

class TransaccionCreateView(CreateView):
    model = Transaccion
    form_class = TransaccionForm
    success_url = reverse_lazy("gestion:transaccion_list")

class TransaccionUpdateView(UpdateView):
    model = Transaccion
    form_class = TransaccionForm
    success_url = reverse_lazy("gestion:transaccion_list")

class TransaccionDetailView(DetailView):
    model = Transaccion

class TransaccionDeleteView(DeleteView):
    model = Transaccion
    success_url = reverse_lazy("gestion:transaccion_list")