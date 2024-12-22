from ..forms import UsuarioForm
from ..models import Usuario
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class UsuarioListView(ListView):
    model = Usuario

class UsuarioCreateView(CreateView):
    model = Usuario
    form_class = UsuarioForm
    success_url = reverse_lazy("gestion:usuario_list")

class UsuarioUpdateView(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    success_url = reverse_lazy("gestion:usuario_list")

class UsuarioDeleteView(DeleteView):
    model = Usuario
    success_url = reverse_lazy("gestion:usuario_list")