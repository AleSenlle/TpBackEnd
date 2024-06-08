from django.urls import path
from .views import ListViewReseñas, DetailViewReseña, CrearReseña
urlpatterns = [
    path('',ListViewReseñas.as_view(), name='list_reseñas'),
    path('detail/<int:pk>/',DetailViewReseña.as_view(), name='detail_reseña'),
    path('crear', CrearReseña.as_view(), name='crear_reseña'),
]