from ..forms import UsuarioForm
from ..models import Usuario
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib import messages


class UsuarioListView(ListView):
    model = Usuario
    def get_queryset(self):
    # Si el usuario es staff, muestra todas las transacciones
        if self.request.user.is_staff:
            return Usuario.objects.all()
    # Si no, solo las del usuario actual
        return Usuario.objects.filter(usuario=self.request.user)

class UsuarioCreateView(CreateView):
    model = Usuario
    form_class = UsuarioForm
    success_url = reverse_lazy("gestion:usuario_list")
    def get_queryset(self):
    # Si el usuario es staff, muestra todas las transacciones
        if self.request.user.is_staff:
            return Usuario.objects.all()
    # Si no, solo las del usuario actual
        return Usuario.objects.filter(usuario=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, 'Usuario creado exitosamente')
        return super().form_valid(form)

class UsuarioUpdateView(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    success_url = reverse_lazy("gestion:usuario_list")
    def get_queryset(self):
    # Si el usuario es staff, muestra todas las transacciones
        if self.request.user.is_staff:
            return Usuario.objects.all()
    # Si no, solo las del usuario actual
        return Usuario.objects.filter(usuario=self.request.user)
    
    def form_valid(self, form):
        messages.success(self.request, 'Usuario actualizado exitosamente')
        return super().form_valid(form)
    
class UsuarioDetailView(DetailView):
    model = Usuario

class UsuarioDeleteView(DeleteView):
    model = Usuario
    success_url = reverse_lazy("gestion:usuario_list")