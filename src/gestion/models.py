from django.db import models
from datetime import datetime, date
from django.contrib.auth.models import User
from django.db.models import Sum
from calendar import monthrange
from django.core.exceptions import ValidationError

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
        ('SEMESTRAL', 'Semestre'),
        ('ANUAL', 'Anual'),
    ]

class Usuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Usuario')
    dni = models.IntegerField(unique=True,null=True)
    fecha_nacimiento = models.DateField()
    foto = models.ImageField(upload_to='imagenes_perfil', blank=True, null=True)

    @property
    def calcular_edad(self):
        hoy = datetime.today()
        if hoy.month < self.fecha_nacimiento.month:
            edad = hoy.year - self.fecha_nacimiento.year -1
        else:
            edad = hoy.year - self.fecha_nacimiento.year
        return edad

    def __str__(self):
        return self.usuario.username

class Transaccion(models.Model):
    nombre = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    tipo = models.CharField(max_length=1,choices=TIPOS_TRANSACCIONES)
    monto = models.DecimalField(max_digits=10,decimal_places=2)
    categoria = models.CharField(max_length=50,choices=CATEGORIAS,default="O")
    descripcion = models.TextField(max_length=30,null=True,blank=True)
    fecha = models.DateField(null=True,blank=True)

    class Meta:
        verbose_name = "Transaccion"
        verbose_name_plural = "Transacciones"
        ordering = ("-fecha",)

class Informe(models.Model):
    nombre = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    año = models.PositiveIntegerField()
    informe = models.CharField(max_length=25)
    tipo = models.CharField(max_length=3,choices=TIPOS_INFORME,default='BAL')
    periodo = models.CharField(max_length=10,choices=PERIODOS,default='ANUAL')
    mes_inicio = models.PositiveIntegerField(default=1)  
    mes_fin = models.PositiveIntegerField(default=12)    

    class Meta():
        unique_together = ("año","tipo","periodo","mes_inicio","mes_fin")

    def clean(self):
        """Valida que mes_inicio y mes_fin sean valores lógicos."""
        if self.mes_inicio and self.mes_fin:
            if not (1 <= self.mes_inicio <= 12) or not (1 <= self.mes_fin <= 12):
                raise ValidationError("Los meses deben estar entre 1 y 12.")
            if self.mes_inicio > self.mes_fin:
                raise ValidationError("El mes de inicio no puede ser mayor que el mes final.")

    def calcular_total_rango(self, inicio, fin):
        suma_ingresos = 0
        suma_gastos = 0
        suma_total = 0
        if self.tipo == 'ING':  # Ingresos
            total = Transaccion.objects.filter(
                nombre=self.nombre,
                tipo='I',
                fecha__range=[inicio, fin]
            )
            suma_total = total.aggregate(total=Sum('monto'))['total'] or 0
            return suma_total, 0, 0
        
        elif self.tipo == 'GAS':  # Gastos
            total = Transaccion.objects.filter(
                nombre=self.nombre,
                tipo='G',
                fecha__range=[inicio, fin]
            )
            suma_total = total.aggregate(total=Sum('monto'))['total'] or 0
            return 0, suma_total, 0
        
        elif self.tipo == 'BAL':  # Balance
            ingresos = Transaccion.objects.filter(
                nombre=self.nombre,
                tipo='I',
                fecha__range=[inicio, fin]
            )
            suma_ingresos = ingresos.aggregate(total=Sum('monto'))['total'] or 0
            gastos = Transaccion.objects.filter(
                nombre=self.nombre,
                tipo='G',
                fecha__range=[inicio, fin]
            )
            suma_gastos = gastos.aggregate(total=Sum('monto'))['total'] or 0
            suma_total = suma_ingresos- suma_gastos
            return suma_ingresos, suma_gastos, suma_total
        else:
            return 0,0,0
    
    def calcular_totales_mensuales(self):
        totales = []
        for mes in range(self.mes_inicio, self.mes_fin + 1):
            inicio_mes = date(self.año, mes, 1)
            _, fin_dia = monthrange(self.año, mes)
            fin_mes = date(self.año, mes, fin_dia)

            ingresos, gastos, total = self.calcular_total_rango(inicio_mes, fin_mes)
            totales.append((inicio_mes.strftime("%b %Y"), ingresos, gastos, total))
        return totales
