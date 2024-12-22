from django.urls import path
from .views import (index, about)
from .views_models import transaccion, usuario, informe

app_name = "gestion"

urlpatterns = [
    path('', index, name="index"),
    path('about/', about, name="about"),]

urlpatterns += [
    path("usuario/list/", usuario.usuario_list, name="usuario_list"),
    path("usuario/create/", usuario.usuario_create, name="usuario_create"),]

urlpatterns += [
    path("transaccion/list/", transaccion.TransaccionListView.as_view(), name="transaccion_list"),
    path("transaccion/create/", transaccion.TransaccionCreateView.as_view(), name="transaccion_create"),
    path("transaccion/update/<int:pk>", transaccion.TransaccionUpdateView.as_view(), name="transaccion_update"),
    path("transaccion/detail/<int:pk>", transaccion.TransaccionDetailView.as_view(), name="transaccion_detail"),
    path("transaccion/delete/<int:pk>", transaccion.TransaccionDeleteView.as_view(), name="transaccion_delete"),]

urlpatterns += [
    path("informe/list/", informe.informe_list, name="informe_list"),
    path("informe/create/", informe.informe_create, name="informe_create"),]
