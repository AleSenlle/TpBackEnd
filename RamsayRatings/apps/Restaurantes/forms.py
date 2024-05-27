from .models import Restaurante


class restauranteForm(forms.ModelForm):
    class Meta:
        model = Restaurante
        fields = '__all__'