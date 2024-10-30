from django import forms
from .models import Restaurante

class RestauranteForm(forms.ModelForm):
    class Meta:
        model = Restaurante
        fields = '__all__'  # Incluye todos los campos, incluyendo 'imagen'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}),
            'direccion': forms.TextInput(attrs={'class': 'appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}),
            'tipo': forms.TextInput(attrs={'class': 'appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}),
            'horario': forms.TextInput(attrs={'class': 'appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}),  # Para el campo de imagen
        }
        labels = {
            'nombre': 'Nombre del Restaurante',
            'direccion': 'Dirección',
            'horario': 'Horario',
            'tipo': 'Tipo de Cocina',
            'imagen': 'Imagen del Restaurante',  # Etiqueta para el campo de imagen
        }

