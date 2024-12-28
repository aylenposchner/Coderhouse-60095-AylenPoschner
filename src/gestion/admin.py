from django.contrib import admin
from . import models

admin.site.register(models.Usuario)

@admin.register(models.Transaccion)
class TransaccionAdmin(admin.ModelAdmin):
    list_display = ("nombre","fecha","tipo","categoria","monto")
    list_display_links = ("nombre",)
    list_filter = ("tipo","categoria")
    search_fields = ("nombre__nombre",)
    list_per_page = 25

@admin.register(models.Informe)
class InformesAdmin(admin.ModelAdmin):
    list_display = ("nombre","año","informe")