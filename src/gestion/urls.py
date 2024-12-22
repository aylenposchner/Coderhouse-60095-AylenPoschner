from django.urls import path
from .views import (index, about)
from .views_models import transaccion, usuario, informe

app_name = "gestion"

urlpatterns = [
    path('', index, name="index"),
    path('about/', about, name="about"),
    path("usuario/list/", usuario.usuario_list, name="usuario_list"),
    path("usuario/create/", usuario.usuario_create, name="usuario_create"),
    path("transaccion/list/", transaccion.transaccion_list, name="transaccion_list"),
    path("transaccion/create/", transaccion.transaccion_create, name="transaccion_create"),
    path("transaccion/update/<int:pk>", transaccion.transaccion_update, name="transaccion_update"),
    path("transaccion/detail/<int:pk>", transaccion.transaccion_detail, name="transaccion_detail"),
    path("transaccion/delete/<int:pk>", transaccion.transaccion_delete, name="transaccion_delete"),
    path("informe/list/", informe.informe_list, name="informe_list"),
    path("informe/create/", informe.informe_create, name="informe_create"),
]
