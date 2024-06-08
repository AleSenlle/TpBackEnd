from django.db import models
from ..Restaurantes.models import Restaurante

class Reseña(models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    comentario = models.TextField()
    valoracion = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre