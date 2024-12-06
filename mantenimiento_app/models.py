from django.db import models

class Mantenimiento(models.Model):
    id_mantenimiento = models.IntegerField(primary_key=True)
    fecha = models.DateField()
    descripcion = models.CharField(max_length=255)
    costo = models.IntegerField()
    id_vehiculo = models.IntegerField()
    id_empleado = models.IntegerField()
    tipo_mantenimiento = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.descripcion
