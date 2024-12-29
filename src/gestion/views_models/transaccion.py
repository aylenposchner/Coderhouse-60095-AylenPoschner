from ..forms import TransaccionForm
from ..models import Transaccion
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy

class TransaccionListView(ListView):
    model = Transaccion
    def get_queryset(self):
    # Si el usuario es staff, muestra todas las transacciones
        if self.request.user.is_staff:
            return Transaccion.objects.all()
    # Si no, solo las del usuario actual
        return Transaccion.objects.filter(nombre=self.request.user)

class TransaccionCreateView(CreateView):
    model = Transaccion
    form_class = TransaccionForm
    success_url = reverse_lazy("gestion:transaccion_list")
    def get_form_kwargs(self):
        # Obtener los argumentos del formulario estándar
        kwargs = super().get_form_kwargs()
        # Agregar el usuario actual al formulario
        kwargs['user'] = self.request.user      
        return kwargs

    def form_valid(self, form):
        # Si el usuario no es staff, asignamos el usuario actual al campo 'nombre'
        if not self.request.user.is_staff:
            form.instance.nombre = self.request.user
        return super().form_valid(form)
    
class TransaccionUpdateView(UpdateView):
    model = Transaccion
    form_class = TransaccionForm
    success_url = reverse_lazy("gestion:transaccion_list")
    def get_queryset(self):
    # Si el usuario es staff, muestra todas las transacciones
        if self.request.user.is_staff:
            return Transaccion.objects.all()
    # Si no, solo las del usuario actual
        return Transaccion.objects.filter(nombre=self.request.user)

class TransaccionDetailView(DetailView):
    model = Transaccion

class TransaccionDeleteView(DeleteView):
    model = Transaccion
    success_url = reverse_lazy("gestion:transaccion_list")