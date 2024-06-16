from django.views.generic.list import ListView
from apps.reseñas.models import Reseña

"""class HomeView(TemplateView):
    def get(self,request,*args,**kwargs):
        context={}
        return render(request,'pages/index.html',context)"""
    
class HomeView(ListView):
    template_name = 'pages/index.html'
    context_object_name = 'ultimas_reseñas'

    def get_queryset(self):
        # Obtener las últimas 3 reseñas
        return Reseña.objects.order_by('-fecha')[:3]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Ramsey Review - Últimas Reseñas'
        return context