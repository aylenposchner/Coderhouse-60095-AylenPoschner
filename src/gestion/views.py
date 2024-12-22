from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .forms import UsuarioForm, TransaccionForm, InformeForm
from .models import Usuario, Transaccion, Informe

def index(request: HttpRequest) -> HttpResponse:
    return render(request, "gestion/index.html")

def about(request: HttpRequest) -> HttpResponse:
    return render(request,"gestion/about.html")

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


def transaccion_list(request: HttpRequest) -> HttpResponse:
    query = Transaccion.objects.all()
    context = {"object_list": query}
    return render(request, "gestion/transaccion_list.html", context)


def transaccion_create(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        form = TransaccionForm()
    if request.method == "POST":
        form = TransaccionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("gestion:transaccion_list")
    return render(request, "gestion/transaccion_form.html", {"form": form})

def transaccion_update(request: HttpRequest, pk:int) -> HttpResponse:
    query = Transaccion.objects.get(id=pk)
    if request.method == "GET":
        form = TransaccionForm(instance=query)
    if request.method == "POST":
        form = TransaccionForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            messages.success(request, 'Transacción actualizada correctamente')
            return redirect("gestion:transaccion_list")
    return render(request, "gestion/transaccion_form.html", {"form": form})

def transaccion_detail(request: HttpRequest, pk: int) -> HttpResponse:
    query = Transaccion.objects.get(id=pk)
    return render(request, 'gestion/transaccion_detail.html', {'object': query})

def transaccion_delete(request: HttpRequest, pk:int) -> HttpResponse:
    query = Transaccion.objects.get(id=pk)
    if request.method == "POST":
        query.delete()
        messages.success(request, 'Transacción eliminada')
        return redirect("gestion:transaccion_list")
    return render(request, "gestion/transaccion_confirm_delete.html", {'object': query})




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