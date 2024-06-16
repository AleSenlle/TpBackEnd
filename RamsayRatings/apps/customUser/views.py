
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic.detail import DetailView
from .forms import CustomUserCreationForm , CustomUserChangeForm
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .decorador import IsNotAuthenticatedMixin


class Registro(IsNotAuthenticatedMixin, CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'registro.html'
    success_url = reverse_lazy('custom_login')

    def form_invalid(self, form):
        response = super().form_invalid(form)
        # Añadir mensajes de error para cada campo del formulario
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"{field}: {error}")
        return response

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, '¡Registro exitoso! Ahora puedes iniciar sesión.')
        return response
    
    
class Perfil(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'perfil.html'

    def get_object(self):
        return self.request.user
    
class UpdateUserTypeView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    template_name = 'update_user_type.html'
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('perfil')

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, '¡Tipo de usuario actualizado!')
        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"{field}: {error}")
        return response