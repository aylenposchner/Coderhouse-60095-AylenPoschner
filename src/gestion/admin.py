from django.contrib import admin
from .models import Usuario, Transaccion, Informe   

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("nombre",)

@admin.register(Transaccion)
class TransaccionAdmin(admin.ModelAdmin):
    list_display = ("fecha","tipo","monto")

@admin.register(Informe)
class InformesAdmin(admin.ModelAdmin):
    list_display = ("año","informe")