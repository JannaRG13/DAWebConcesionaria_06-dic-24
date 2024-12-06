from django.db import models

class Venta(models.Model):
    id_venta = models.IntegerField(primary_key=True)
    fecha = models.DateField()
    precio = models.IntegerField()
    forma_pago = models.CharField(max_length=255)
    id_vehiculo = models.IntegerField()
    id_cliente = models.IntegerField()
    id_empleado = models.IntegerField()

    def __str__(self) -> str:
        return self.fecha