from .models import Reseña
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .forms import reseñaForm
from ..Restaurantes.models import Restaurante
from ..customUser.decorador import ReseñadorRequiredMixin
from datetime import datetime

class ListViewReseñas(ListView):
    model = Reseña
    template_name = 'list_reseñas.html'
    paginate_by = 3

class DetailViewReseña(DetailView):
    model = Reseña
    template_name = 'detail_reseña.html'

#form_valid() asigna el usuario que está creando la reseña
class CrearReseña(ReseñadorRequiredMixin, CreateView):
    model = Reseña
    template_name = 'crear_reseña.html'
    form_class = reseñaForm
    success_url = reverse_lazy('list_reseñas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['restaurantes'] = Restaurante.objects.all()
        return context

    def form_valid(self, form):
        form.instance.usuario = self.request.user  # Asignar el usuario actual al campo 'usuario'
        form.instance.fecha = datetime.now()  # Asignar la fecha actual al campo 'fecha'
        return super().form_valid(form)
    
#Se sobreescribe el método get_queryset() para que solo se muestren las reseñas del usuario que está logueado 
class DeleteReseña(ReseñadorRequiredMixin, DeleteView): 
    model = Reseña 
    template_name = 'delete_reseña.html' 
    success_url = reverse_lazy('list_reseñas') 
 
    def get_queryset(self): 
        queryset = super().get_queryset() 
        return queryset.filter(usuario=self.request.user) 
 
#Se sobreescribe el método get_context_data() para que se muestren los restaurantes en el formulario  
class UpdateReseña(ReseñadorRequiredMixin, UpdateView): 
    model = Reseña 
    template_name = 'update_reseña.html' 
    form_class = reseñaForm 
    success_url = reverse_lazy('list_reseñas') 
 
    def get_queryset(self): 
        queryset = super().get_queryset() 
        return queryset.filter(usuario=self.request.user) 
 
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
        context['restaurantes'] = Restaurante.objects.all() 
        return context