from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Restaurante
from .forms import restauranteForm
from django.urls import reverse_lazy

class DetailViewRestaurante(DetailView):
    model = Restaurante
    template_name = 'detail_restaurante.html'

class ListViewRestaurante(ListView):
    model = Restaurante
    template_name = 'list_restaurante.html'
    paginate_by = 6

class CrearRestaurante(CreateView):
    model = Restaurante
    template_name = 'crear_restaurante.html'
    form_class = restauranteForm
    success_url = reverse_lazy('list_restaurante')
