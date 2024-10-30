
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from .models import Restaurante
from .forms import RestauranteForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, HttpResponseRedirect
from ..customUser.decorador import RestaurantesRequiredMixin


class DetailViewRestaurante(DetailView):
    model = Restaurante
    template_name = 'detail_restaurante.html'

class ListViewRestaurante(ListView):
    model = Restaurante
    template_name = 'list_restaurante.html'
    paginate_by = 6

class CrearRestaurante(RestaurantesRequiredMixin, CreateView):
    model = Restaurante
    template_name = 'crear_restaurante.html'
    form_class = RestauranteForm
    success_url = reverse_lazy('list_restaurante')

class DeleteRestaurante(RestaurantesRequiredMixin, DeleteView):
    model = Restaurante
    template_name = 'delete_restaurante.html'
    success_url = reverse_lazy('list_restaurante')

class UpdateRestaurante(RestaurantesRequiredMixin, UpdateView):
    model = Restaurante
    form_class = RestauranteForm
    template_name = 'update_restaurante.html'
    context_object_name = 'restaurante'
    success_url = reverse_lazy('list_restaurante')

class UpdateRestaurante(RestaurantesRequiredMixin, UpdateView):
    model = Restaurante
    form_class = RestauranteForm
    template_name = 'update_restaurante.html'
    context_object_name = 'restaurante'
    success_url = reverse_lazy('list_restaurante')
