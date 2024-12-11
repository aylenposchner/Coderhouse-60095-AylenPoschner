from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=15, unique=True)

class Transaccion(models.Model):
    tipo_transaccion =[("I","Ingreso"),("G","Gasto")]
    tipo = models.CharField(max_length=1,choices=tipo_transaccion)
    monto = models.DecimalField(max_digits=10,decimal_places=2)
    descripcion = models.TextField(max_length=50,null=True,blank=True)
    fecha = models.DateField(null=True,blank=True)

class Informe(models.Model):
    año = models.PositiveIntegerField()
    informe = models.CharField(max_length=25)

    class Meta():
        constraints = [models.UniqueConstraint(fields=["año","informe"], name="unico_informe_por_año")]