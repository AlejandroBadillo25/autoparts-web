from django.shortcuts import redirect
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import JsonResponse
from django.views.generic import FormView, View, UpdateView
from django.urls import reverse_lazy
from .forms import LoginForm, RegisterForm, ProfileEditForm, ChangePasswordForm
from .models import UserProfile


# ==================== AUTHENTICATION VIEWS ====================

class LoginView(FormView):
    """Vista para login de usuarios"""
    form_class = LoginForm
    template_name = 'accountsApp/login.html'
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('autopartsApp:home')
        return super().dispatch(request, *args, **kwargs)
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs
    
    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            messages.success(self.request, f'¡Bienvenido {username}!')
            return redirect('autopartsApp:home')
        return super().form_valid(form)


class RegisterView(FormView):
    """Vista para registro de nuevos usuarios"""
    form_class = RegisterForm
    template_name = 'accountsApp/register.html'
    success_url = reverse_lazy('accountsApp:login')
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('autopartsApp:home')
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        user = form.save()
        # Crear perfil de usuario automáticamente
        UserProfile.objects.create(user=user)
        messages.success(self.request, 'Cuenta creada exitosamente')
        return super().form_valid(form)


class LogoutView(View):
    """Vista para cerrar sesión"""
    def get(self, request):
        logout(request)
        messages.info(request, 'Has cerrado sesión exitosamente.')
        return redirect('autopartsApp:home')
    
    def post(self, request):
        return self.get(request)


# ==================== PROFILE VIEWS ====================

class ProfileEditView(LoginRequiredMixin, FormView):
    """Vista para editar perfil de usuario"""
    form_class = ProfileEditForm
    template_name = 'accountsApp/profile_edit.html'
    success_url = reverse_lazy('accountsApp:profile_edit')
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.request.user
        return kwargs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Crear perfil si no existe
        profile, created = UserProfile.objects.get_or_create(user=self.request.user)
        context['profile'] = profile
        return context
    
    def form_valid(self, form):
        user = form.save()
        
        # Actualizar o crear perfil con phone, address y profile_image
        profile, created = UserProfile.objects.get_or_create(user=self.request.user)
        profile.phone = form.cleaned_data.get('phone')
        profile.address = form.cleaned_data.get('address')
        
        # Guardar imagen de perfil si fue proporcionada
        if 'profile_image' in self.request.FILES:
            profile.profile_image = self.request.FILES['profile_image']
        
        profile.save()
        
        messages.success(self.request, 'Perfil actualizado exitosamente.')
        return super().form_valid(form)


class ChangePasswordView(LoginRequiredMixin, View):
    """Vista para cambiar contraseña"""
    
    def post(self, request):
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            new_password = form.cleaned_data.get('new_password1')
            request.user.set_password(new_password)
            request.user.save()
            update_session_auth_hash(request, request.user)  # Mantener la sesión activa
            
            # Respuesta para AJAX
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'message': 'Contraseña actualizada exitosamente.'})
            
            messages.success(request, 'Contraseña actualizada exitosamente.')
            return redirect('accountsApp:profile_edit')
        else:
            # Respuesta para AJAX con errores
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': form.errors})
            
            messages.error(request, 'Error al actualizar la contraseña.')
        
        return redirect('accountsApp:profile_edit')
