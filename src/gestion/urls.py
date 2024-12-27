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
    path("informe/list/", informe.InformeListView.as_view(), name="informe_list"),
    path("informe/create/", informe.InformeCreateView.as_view(), name="informe_create"),
    path("informe/update/<int:pk>", informe.InformeUpdateView.as_view(), name="informe_update"),
    path("informe/detail/<int:pk>", informe.InformeDetailView.as_view(), name="informe_detail"),
    path("informe/delete/<int:pk>/", informe.InformeDeleteView.as_view(), name="informe_delete"),
    ]
