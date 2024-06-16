from django.urls import path
from .views import Registro
from .views import Perfil, UpdateUserTypeView

urlpatterns = [
    path('registro', Registro.as_view(), name='registro'),
    path('', Perfil.as_view(), name='perfil'),
    path('actualizar-tipo/', UpdateUserTypeView.as_view(), name='update_user_type'),
]