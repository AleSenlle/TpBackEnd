from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Restaurante

class CrearRestaurante(CreateView):
    model = Restaurante
    fields = ['nombre', 'direccion', 'telefono', 'email', 'tipo']
    template_name = 'Restaurantes/crear_restaurante.html'
    success_url = '/'

class DetailViewRestaurante(DetailView):
    model = Restaurante
    template_name = 'detail_restaurante.html'

class ListViewRestaurante(ListView):
    model = Restaurante
    template_name = 'list_restaurante.html'

