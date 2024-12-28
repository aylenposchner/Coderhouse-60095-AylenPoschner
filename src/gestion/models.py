from django.db import models
from datetime import datetime, date
from django.contrib.auth.models import User
from django.db.models import Sum
from calendar import monthrange

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
    nombre = models.ForeignKey(Usuario,on_delete=models.DO_NOTHING)
    tipo = models.CharField(max_length=1,choices=TIPOS_TRANSACCIONES)
    monto = models.DecimalField(max_digits=10,decimal_places=2)
    categoria = models.CharField(max_length=50,choices=CATEGORIAS,default="O")
    descripcion = models.TextField(max_length=50,null=True,blank=True)
    fecha = models.DateField(null=True,blank=True)

    class Meta:
        verbose_name = "Transaccion"
        verbose_name_plural = "Transacciones"
        ordering = ("-fecha",)

class Informe(models.Model):
    nombre = models.ForeignKey(Usuario,on_delete=models.CASCADE,null=True)
    año = models.PositiveIntegerField()
    informe = models.CharField(max_length=25)
    tipo = models.CharField(max_length=3,choices=TIPOS_INFORME,default='BAL')
    periodo = models.CharField(max_length=10,choices=PERIODOS,default='ANUAL')

    class Meta():
        unique_together = ("año","tipo","periodo")
    
    def calcular_totales_periodo(self):
        if self.periodo == 'MENSUAL':
             return self._calcular_totales_mensuales(1)

        elif self.periodo == 'TRIMESTRAL':
            # Últimos 3 meses
            return self._calcular_totales_mensuales(3)
        
        elif self.periodo == 'SEMESTRAL':
            # Últimos 6 meses
            return self._calcular_totales_mensuales(3)

        elif self.periodo == 'ANUAL':
            # Últimos 12 meses
            return self._calcular_totales_mensuales(12)

        return []

    def _calcular_totales_mensuales(self, meses):
        hoy = date.today()
        totales = []
        for i in range(meses):
            mes = (hoy.month - i - 1) % 12 + 1
            año = hoy.year - ((hoy.month - i - 1) // 12)
            inicio_mes = date(año, mes, 1)
            _, fin_dia = monthrange(año, mes)
            fin_mes = date(año, mes, fin_dia)
            ingresos, gastos, total = self._calcular_total_rango(inicio_mes, fin_mes)
            totales.append((inicio_mes.strftime("%b %Y"), ingresos, gastos, total))
        totales.reverse()
        return totales

    def _calcular_total_rango(self, inicio, fin):
        suma_ingresos = 0
        suma_gastos = 0
        total = 0
        total = 0
        if self.tipo == 'ING':  # Ingresos
            total = Transaccion.objects.filter(
                nombre=self.nombre,
                tipo='I',
                fecha__range=[inicio, fin]
            )
            suma_total = total.aggregate(total=Sum('monto'))['total'] or 0
            return suma_total, 0, suma_total
        
        elif self.tipo == 'GAS':  # Gastos
            total = Transaccion.objects.filter(
                nombre=self.nombre,
                tipo='G',
                fecha__range=[inicio, fin]
            )
            suma_total = total.aggregate(total=Sum('monto'))['total'] or 0
            return 0, suma_total, suma_total
        
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
