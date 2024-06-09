from django.urls import path
from .views import ListViewReseñas, DetailViewReseña, CrearReseña, DeleteReseña, UpdateReseña

urlpatterns = [
    path('',ListViewReseñas.as_view(), name='list_reseñas'),
    path('detail/<int:pk>/',DetailViewReseña.as_view(), name='detail_reseña'),
    path('crear', CrearReseña.as_view(), name='crear_reseña'),
    path('delete/<int:pk>/', DeleteReseña.as_view(), name='delete_reseña'),
    path('update/<int:pk>/', UpdateReseña.as_view(), name='update_reseña'),
]