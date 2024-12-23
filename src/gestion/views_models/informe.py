from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from ..forms import InformeForm
from ..models import Informe
from django.urls import reverse_lazy


class InformeListView(ListView):
    model = Informe
    template_name = "gestion/informe_list.html"
    context_object_name = "object_list"

class InformeCreateView(CreateView):
    model = Informe
    form_class = InformeForm
    success_url = reverse_lazy("gestion:informe_list")

class InformeUpdateView(UpdateView):
    model = Informe
    form_class = InformeForm
    success_url = reverse_lazy("gestion:informe_list")

class InformeDetailView(DetailView):
    model = Informe

class InformeDeleteView(DeleteView):
    model = Informe
    success_url = reverse_lazy("gestion:informe_list")