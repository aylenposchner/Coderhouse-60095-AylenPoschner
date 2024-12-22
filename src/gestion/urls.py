from django.urls import path
from .views import (index, about, usuario_create,usuario_list,transaccion_create,transaccion_list, transaccion_update, transaccion_detail, transaccion_delete, informe_create,informe_list)

app_name = "gestion"

urlpatterns = [
    path('', index, name="index"),
    path('about/', about, name="about"),
    path("usuario/list/", usuario_list, name="usuario_list"),
    path("usuario/create/", usuario_create, name="usuario_create"),
    path("transaccion/list/", transaccion_list, name="transaccion_list"),
    path("transaccion/create/", transaccion_create, name="transaccion_create"),
    path("transaccion/update/<int:pk>", transaccion_update, name="transaccion_update"),
    path("transaccion/detail/<int:pk>", transaccion_detail, name="transaccion_detail"),
    path("transaccion/delete/<int:pk>", transaccion_delete, name="transaccion_delete"),
    path("informe/list/", informe_list, name="informe_list"),
    path("informe/create/", informe_create, name="informe_create"),
]
