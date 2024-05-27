from django.db import models

class Restaurante(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    email = models.EmailField()
    tipo = models.CharField(max_length=50)
   
    def __str__(self):
        return self.nombre
