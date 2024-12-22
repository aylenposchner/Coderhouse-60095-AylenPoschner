from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from ..forms import UsuarioForm
from ..models import Usuario

def usuario_list(request: HttpRequest) -> HttpResponse:
    query = Usuario.objects.all()
    context = {"object_list": query}
    return render(request, "gestion/usuario_list.html", context)


def usuario_create(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        form = UsuarioForm()
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("gestion:usuario_list")
    return render(request, "gestion/usuario_form.html", {"form": form})