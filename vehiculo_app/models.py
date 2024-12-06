from django.db import models

class Vehiculo(models.Model):
    id_vehiculo = models.IntegerField(primary_key=True)
    marca = models.CharField(max_length=255)
    modelo = models.CharField(max_length=255)
    anio = models.IntegerField()
    color = models.CharField(max_length=255)
    precio = models.IntegerField()
    kilometraje = models.IntegerField()

    def __str__(self) -> str:
        return self.marca
