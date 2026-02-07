from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from .models import Banner
from .forms import BannerForm


# ==================== MIXIN PERSONALIZADO ====================

class StaffOrSuperuserRequiredMixin(UserPassesTestMixin):
    """Mixin que verifica si el usuario es staff o superuser"""
    login_url = 'autopartsApp:home'
    
    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser


# ==================== BANNER VIEWS ====================

class BannerListView(LoginRequiredMixin, StaffOrSuperuserRequiredMixin, ListView):
    """Lista todos los banners"""
    model = Banner
    template_name = 'autopartsBannersApp/banner_list.html'
    context_object_name = 'banners'


class BannerCreateView(LoginRequiredMixin, StaffOrSuperuserRequiredMixin, CreateView):
    """Crea un nuevo banner"""
    model = Banner
    form_class = BannerForm
    template_name = 'autopartsBannersApp/banner_form.html'
    success_url = reverse_lazy('autopartsBannersApp:banner_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Nuevo Banner'
        return context
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        messages.success(self.request, 'Banner creado exitosamente.')
        return super().form_valid(form)


class BannerUpdateView(LoginRequiredMixin, StaffOrSuperuserRequiredMixin, UpdateView):
    """Edita un banner existente"""
    model = Banner
    form_class = BannerForm
    template_name = 'autopartsBannersApp/banner_form.html'
    success_url = reverse_lazy('autopartsBannersApp:banner_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Banner'
        context['banner'] = self.object
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'Banner actualizado exitosamente.')
        return super().form_valid(form)


class BannerDeleteView(LoginRequiredMixin, StaffOrSuperuserRequiredMixin, DeleteView):
    """Elimina un banner"""
    model = Banner
    template_name = 'autopartsBannersApp/banner_confirm_delete.html'
    context_object_name = 'banner'
    success_url = reverse_lazy('autopartsBannersApp:banner_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Banner eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)


class BannerToggleActiveView(LoginRequiredMixin, StaffOrSuperuserRequiredMixin, View):
    """Activa/desactiva un banner"""
    
    def post(self, request, pk):
        banner = get_object_or_404(Banner, pk=pk)
        banner.is_active = not banner.is_active
        banner.save()
        status = 'activado' if banner.is_active else 'desactivado'
        messages.success(request, f'Banner {status} exitosamente.')
        return redirect('autopartsBannersApp:banner_list')
    
    def get(self, request, pk):
        return self.post(request, pk)
