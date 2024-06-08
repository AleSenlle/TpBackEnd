from django import forms
from .models import Reseña

class reseñaForm(forms.ModelForm):
    class Meta:
        model = Reseña
        fields = '__all__'
        widgets = {
            'restaurante': forms.Select(attrs={'class':'form-control'}),
            'puntuacion': forms.NumberInput(attrs={'class':'form-control'}),
            'comentario': forms.Textarea(attrs={'class':'form-control'}),
            'fecha': forms.DateInput(attrs={'class':'form-control'}),
            'usuario': forms.TextInput(attrs={'class':'form-control'}),
        }