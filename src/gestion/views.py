from django.shortcuts import render, redirect
from .forms import UsuarioForm, TransaccionForm, InformeForm
from .models import Usuario, Transaccion, Informe

def index(request):
    return render(request, "gestion/index.html")

def about(request):
    return render(request,"gestion/about.html")

def usuario_list(request):
    query = Usuario.objects.all()
    context = {"object_list": query}
    return render(request, "gestion/usuario_list.html", context)


def usuario_create(request):
    if request.method == "GET":
        form = UsuarioForm()
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("gestion:usuario_list")
    return render(request, "gestion/usuario_form.html", {"form": form})


def transaccion_list(request):
    query = Transaccion.objects.all()
    context = {"object_list": query}
    return render(request, "gestion/transaccion_list.html", context)


def transaccion_create(request):
    if request.method == "GET":
        form = TransaccionForm()
    if request.method == "POST":
        form = TransaccionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("gestion:transaccion_list")
    return render(request, "gestion/transaccion_form.html", {"form": form})


def informe_list(request):
    query = Informe.objects.all()
    context = {"object_list": query}
    return render(request, "gestion/informe_list.html", context)


def informe_create(request):
    if request.method == "GET":
        form = InformeForm()
    if request.method == "POST":
        form = InformeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("gestion:informe_list")
    return render(request, "gestion/informe_form.html", {"form": form})