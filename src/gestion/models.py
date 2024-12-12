from django.db import models

# def normalizar_texto(texto: str) -> str:
#     """Transforma el texto a una forma normalizada NFD
#     (Normalization Form Decomposition).
#     Esto significa que los caracteres compuestos,
#     como las letras con tildes o diacríticos,
#     se descomponen en su forma base y sus marcas diacríticas separadas.
#     Ej: la letra "é" se descompone en "e" + un carácter de tilde combinable (U+0301).
#     Convierte la cadena en bytes usando la codificación ASCII.
#     Si un carácter no puede representarse en ASCII (por ejemplo, una "ñ" o una "é"),
#     se ignora debido al parámetro "ignore".
#     Luego, convierte los bytes resultantes nuevamente a una cadena de texto utilizando la codificación UTF-8."""
#     texto = unicodedata.normalize("NFD", texto)
#     texto = texto.encode("ascii", "ignore").decode("utf-8")
#     return texto

class Usuario(models.Model):
    nombre = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.nombre

class Transaccion(models.Model):
    nombre = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    tipo_transaccion =[("I","Ingreso"),("G","Gasto")]
    tipo = models.CharField(max_length=1,choices=tipo_transaccion)
    monto = models.DecimalField(max_digits=10,decimal_places=2)
    categorias = [("A","Alimentos"),
                 ("AS","Alquiler y Servicios"),
                 ("S","Shopping"),
                 ("R","Regalos"),
                 ("E","Entretenimiento"),
                 ("V","Viajes"),
                 ("S","Sueldo"),
                 ("O","Otros")]
    categoria = models.CharField(max_length=50,choices=categorias,default="O")
    descripcion = models.TextField(max_length=50,null=True,blank=True)
    fecha = models.DateField(null=True,blank=True)

class Informe(models.Model):
    nombre = models.ForeignKey(Usuario,on_delete=models.CASCADE,null=True)
    año = models.PositiveIntegerField()
    informe = models.CharField(max_length=25)
    categorias = [
        ('ING', 'Ingreso'),
        ('GAS', 'Gasto'),
        ('BAL', 'Balance General'),
    ]
    categoria = models.CharField(max_length=3,choices=categorias,default='BAL')
    periodos = [
        ('MENSUAL', 'Mensual'),
        ('TRIMESTRAL', 'Trimestral'),
        ('ANUAL', 'Anual'),
    ]
    periodo = models.CharField(max_length=10,choices=periodos,default='ANUAL')


    class Meta():
        constraints = [models.UniqueConstraint(fields=["año","categoria","periodo"], name="unico_informe_por_año")]