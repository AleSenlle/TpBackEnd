from django.urls import path
from .views import ListViewRestaurante, DetailViewRestaurante, CrearRestaurante, DeleteRestaurante, UpdateRestaurante
urlpatterns = [
    path('',ListViewRestaurante.as_view(), name='list_restaurante'),
    path('detail/<int:pk>/',DetailViewRestaurante.as_view(), name='detail_restaurante'),
    path('crear', CrearRestaurante.as_view(), name='crear_restaurante'),
    path('delete/<int:pk>/', DeleteRestaurante.as_view(), name='delete_restaurante'),
    path('update/<int:pk>/', UpdateRestaurante.as_view(), name='update_restaurante'),
    
    
]