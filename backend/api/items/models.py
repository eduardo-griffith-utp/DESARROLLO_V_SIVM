from django.db import models

class Item(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    contraseña = models.CharField(max_length=128)

    def __str__(self):
        return self.nombre
