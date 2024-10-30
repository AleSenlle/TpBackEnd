from django.views.generic.list import ListView
from apps.reseñas.models import Reseña

class HomeView(ListView):
    template_name = 'pages/index.html'
    context_object_name = 'ultimas_reseñas'

    def get_queryset(self):
        # Obtener las últimas 3 reseñas, cargando los datos de restaurantes relacionados
        return Reseña.objects.select_related('restaurante').order_by('-fecha')[:3]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Ramsey Review - Últimas Reseñas'
        return context
