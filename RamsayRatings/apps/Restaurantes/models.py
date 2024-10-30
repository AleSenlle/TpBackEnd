from django.db import models

class Restaurante(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='restaurantes/', null=True, blank=True)

    def __str__(self):
        return self.nombre
