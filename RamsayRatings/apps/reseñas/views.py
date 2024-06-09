from django.shortcuts import render
from .models import Reseña
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .forms import reseñaForm
from ..Restaurantes.models import Restaurante

class ListViewReseñas(ListView):
    model = Reseña
    template_name = 'list_reseñas.html'
    paginate_by = 3

class DetailViewReseña(DetailView):
    model = Reseña
    template_name = 'detail_reseña.html'

class CrearReseña(CreateView):
    model = Reseña
    template_name = 'crear_reseña.html'
    form_class = reseñaForm
    success_url = reverse_lazy('list_reseñas')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['restaurantes'] = Restaurante.objects.all()
        return context

class DeleteReseña(DeleteView):
    model = Reseña
    template_name = 'delete_reseña.html'
    success_url = reverse_lazy('list_reseñas')

class UpdateReseña(UpdateView):
    model = Reseña
    template_name = 'update_reseña.html'
    form_class = reseñaForm
    success_url = reverse_lazy('list_reseñas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['restaurantes'] = Restaurante.objects.all()
        return context