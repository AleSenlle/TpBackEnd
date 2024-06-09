from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('reseñador', 'reseñador'),
        ('observador', 'observador'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='observador')

    def __str__(self):
        return self.username

