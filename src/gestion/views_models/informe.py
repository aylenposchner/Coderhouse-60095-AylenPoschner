from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from ..forms import InformeForm
from ..models import Informe

def informe_list(request: HttpRequest) -> HttpResponse:
    query = Informe.objects.all()
    context = {"object_list": query}
    return render(request, "gestion/informe_list.html", context)


def informe_create(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        form = InformeForm()
    if request.method == "POST":
        form = InformeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("gestion:informe_list")
    return render(request, "gestion/informe_form.html", {"form": form})