from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

class IsNotAuthenticatedMixin(UserPassesTestMixin):
    def test_func(self):
        return not self.request.user.is_authenticated
    
    def handle_no_permission(self):
        return HttpResponseRedirect(reverse_lazy('perfil'))

class ReseñadorRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if request.user.user_type != 'reseñador':
            messages.error(request, "No tienes permisos para acceder a esta página.")
            return redirect(reverse('custom_login'))  # Usar 'custom_login' en lugar de 'login'
        return super().dispatch(request, *args, **kwargs)

class RestaurantesRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if request.user.is_staff == False:
            messages.error(request, "No tienes permisos para acceder a esta página.")
            return redirect(reverse('custom_login'))  # Usar 'custom_login' en lugar de 'login'
        return super().dispatch(request, *args, **kwargs)