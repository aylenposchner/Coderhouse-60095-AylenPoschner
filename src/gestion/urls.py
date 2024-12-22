from django.urls import path
from .views_models import transaccion, usuario, informe

app_name = "gestion"

urlpatterns = [
    path("usuario/list/", usuario.UsuarioListView.as_view(), name="usuario_list"),
    path("usuario/create/", usuario.UsuarioCreateView.as_view(), name="usuario_create"),
    path("usuario/update/<int:pk>", usuario.UsuarioUpdateView.as_view(), name="usuario_update"),
    path("usuario/delete/<int:pk>/", usuario.UsuarioDeleteView.as_view(), name="usuario_delete"),
    ]

urlpatterns += [
    path("transaccion/list/", transaccion.TransaccionListView.as_view(), name="transaccion_list"),
    path("transaccion/create/", transaccion.TransaccionCreateView.as_view(), name="transaccion_create"),
    path("transaccion/update/<int:pk>", transaccion.TransaccionUpdateView.as_view(), name="transaccion_update"),
    path("transaccion/detail/<int:pk>", transaccion.TransaccionDetailView.as_view(), name="transaccion_detail"),
    path("transaccion/delete/<int:pk>", transaccion.TransaccionDeleteView.as_view(), name="transaccion_delete"),]

urlpatterns += [
    path("informe/list/", informe.informe_list, name="informe_list"),
    path("informe/create/", informe.informe_create, name="informe_create"),]
