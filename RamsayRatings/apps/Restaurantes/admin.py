from django.contrib import admin
from .models import Restaurante

class RestauranteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'telefono', 'email', 'tipo')
    search_fields = ('nombre', 'direccion', 'telefono', 'email', 'tipo')
admin.site.register(Restaurante)
