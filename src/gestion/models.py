from django.db import models
from datetime import datetime

TIPOS_TRANSACCIONES =[("I","Ingreso"),("G","Gasto")]

CATEGORIAS = [("A","Alimentos"),
             ("AS","Alquiler y Servicios"),
             ("S","Shopping"),
             ("R","Regalos"),
             ("E","Entretenimiento"),
             ("V","Viajes"),
             ("S","Sueldo"),
             ("O","Otros")]

TIPOS_INFORME = [
    ('ING', 'Ingreso'),
    ('GAS', 'Gasto'),
    ('BAL', 'Balance General'),
]

PERIODOS = [
    ('MENSUAL', 'Mensual'),
    ('TRIMESTRAL', 'Trimestral'),
    ('ANUAL', 'Anual'),
]

class Usuario(models.Model):
    nombre = models.CharField(max_length=15)
    dni = models.IntegerField(unique=True,null=True)
    fecha_nacimiento = models.DateField()

    @property
    def calcular_edad(self):
        hoy = datetime.today()
        if hoy.month < self.fecha_nacimiento.month:
            edad = hoy.year - self.fecha_nacimiento.year -1
        else:
            edad = hoy.year - self.fecha_nacimiento.year
        return edad

    def __str__(self):
        return self.nombre

class Transaccion(models.Model):
    nombre = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    tipo = models.CharField(max_length=1,choices=TIPOS_TRANSACCIONES)
    monto = models.DecimalField(max_digits=10,decimal_places=2)
    categoria = models.CharField(max_length=50,choices=CATEGORIAS,default="O")
    descripcion = models.TextField(max_length=50,null=True,blank=True)
    fecha = models.DateField(null=True,blank=True)

    class Meta:
        verbose_name = "Transaccion"
        verbose_name_plural = "Transacciones"

class Informe(models.Model):
    nombre = models.ForeignKey(Usuario,on_delete=models.CASCADE,null=True)
    año = models.PositiveIntegerField()
    informe = models.CharField(max_length=25)
    tipo = models.CharField(max_length=3,choices=TIPOS_INFORME,default='BAL')
    periodo = models.CharField(max_length=10,choices=PERIODOS,default='ANUAL')

    class Meta():
        unique_together = ("año","tipo","periodo")