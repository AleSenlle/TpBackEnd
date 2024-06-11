from django import forms
from .models import Reseña

class reseñaForm(forms.ModelForm):
    class Meta:
        model = Reseña
        exclude = ['usuario', 'fecha']  # Excluir campos 'usuario' y 'fecha' del formulario
        widgets = {
            'restaurante': forms.Select(attrs={'class': 'form-control'}),
            'valoracion': forms.NumberInput(attrs={'class': 'form-control'}),
            'comentario': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def clean_fecha(self):
        return self.instance.fecha
