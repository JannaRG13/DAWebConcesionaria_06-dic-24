from django.db import models

class Agencia(models.Model):
    id_agencia = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    telefono = models.IntegerField()
    email = models.CharField(max_length=255)
    sucursal = models.CharField(max_length=255)
    horario = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.nombre
