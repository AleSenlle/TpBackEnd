from django.db import models
from ..Restaurantes.models import Restaurante
from django.conf import settings

class Reseña(models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    comentario = models.TextField()
    valoracion = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Relación con CustomUser

    def __str__(self):
        return self.nombre