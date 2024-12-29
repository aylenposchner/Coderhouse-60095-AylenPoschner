from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from ..forms import InformeForm
from ..models import Informe
from django.urls import reverse_lazy


class InformeListView(ListView):
    model = Informe
    template_name = "gestion/informe_list.html"
    context_object_name = "object_list"

    def get_queryset(self):
    # Si el usuario es staff, muestra todas las transacciones
        if self.request.user.is_staff:
            return Informe.objects.all()
    # Si no, solo las del usuario actual
        return Informe.objects.filter(nombre=self.request.user)

    
class InformeCreateView(CreateView):
    model = Informe
    form_class = InformeForm
    success_url = reverse_lazy("gestion:informe_list")
    
    def get_form_kwargs(self):
        # Obtener los argumentos del formulario estándar
        kwargs = super().get_form_kwargs()
        # Agregar el usuario actual al formulario
        kwargs['user'] = self.request.user      
        return kwargs

class InformeUpdateView(UpdateView):
    model = Informe
    form_class = InformeForm
    success_url = reverse_lazy("gestion:informe_list")
    def get_queryset(self):
    # Si el usuario es staff, muestra todas las transacciones
        if self.request.user.is_staff:
            return Informe.objects.all()
    # Si no, solo las del usuario actual
        return Informe.objects.filter(nombre=self.request.user)

class InformeDetailView(DetailView):
    model = Informe
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        informe = self.get_object()  # Obtener el informe actual

        # Llamar a calcular_totales_periodo() sobre la instancia 'informe'
        totales_periodo = informe.calcular_totales_mensuales()

        etiquetas = [etiqueta for etiqueta, _, _, _ in totales_periodo]
        ingresos = [float(ingresos) for _, ingresos, _, _,  in totales_periodo]
        gastos = [float(gastos) for _, _, gastos, _ in totales_periodo]
        total = [float(total) for _, _, _, total in totales_periodo]
        # Desestructurar los totales de la forma que necesites
        context['etiquetas'] = etiquetas
        context['total'] = total
        context['ingresos'] = ingresos
        context['gastos'] = gastos

        return context
class InformeDeleteView(DeleteView):
    model = Informe
    success_url = reverse_lazy("gestion:informe_list")