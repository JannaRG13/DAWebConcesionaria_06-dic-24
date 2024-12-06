from django.db import models

class Empleado(models.Model):
    id_empleado = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    curp = models.CharField(max_length=200)
    cargo = models.CharField(max_length=255)
    sueldo = models.IntegerField()
    fecha_ingreso = models.DateField()

    def __str__(self) -> str:
        return self.nombre
