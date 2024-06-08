from .models import Restaurante
from django import forms


class restauranteForm(forms.ModelForm):
    class Meta:
        model = Restaurante
        fields = '__all__'