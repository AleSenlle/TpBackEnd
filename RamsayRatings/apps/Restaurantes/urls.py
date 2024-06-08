from django.urls import path
from .views import ListViewRestaurante, DetailViewRestaurante, CrearRestaurante
urlpatterns = [
    path('',ListViewRestaurante.as_view(), name='list_restaurante'),
    path('detail/<int:pk>/',DetailViewRestaurante.as_view(), name='detail_restaurante'),
    path('crear', CrearRestaurante.as_view(), name='crear_restaurante'),
    
]