from django.contrib import admin
from .models import Reseña

class ReseñaAdmin(admin.ModelAdmin):
    list_display = ('restaurante', 'nombre', 'comentario', 'valoracion', 'fecha')
    search_fields = ('restaurante', 'nombre', 'comentario', 'valoracion', 'fecha')
admin.site.register(Reseña)