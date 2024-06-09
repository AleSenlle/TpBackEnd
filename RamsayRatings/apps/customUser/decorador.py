from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

class ReseñadorRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if request.user.user_type != 'reseñador':
            messages.error(request, "No tienes permisos para acceder a esta página.")
            return redirect(reverse('custom_login'))  # Usar 'custom_login' en lugar de 'login'
        return super().dispatch(request, *args, **kwargs)