from django.db import models

class Cliente(models.Model):
    id_cliente = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    curp = models.CharField(max_length=225)
    direccion = models.CharField(max_length=255)
    telefono = models.IntegerField()
    fecha_nacimiento = models.DateField()

    def __str__(self) -> str:
        return self.nombre
