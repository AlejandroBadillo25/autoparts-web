from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Banner
from .forms import BannerForm

# Create your views here.

def is_staff_or_superuser(user):
    """Verifica si el usuario tiene permisos para gestionar banners"""
    return user.is_staff or user.is_superuser

@login_required
@user_passes_test(is_staff_or_superuser, login_url='autopartsApp:home')
def banner_list(request):
    """Lista todos los banners"""
    banners = Banner.objects.all()
    return render(request, 'autopartsBannersApp/banner_list.html', {'banners': banners})

@login_required
@user_passes_test(is_staff_or_superuser, login_url='autopartsApp:home')
def banner_create(request):
    """Crea un nuevo banner"""
    if request.method == 'POST':
        form = BannerForm(request.POST, request.FILES)
        if form.is_valid():
            banner = form.save(commit=False)
            banner.created_by = request.user
            banner.save()
            messages.success(request, 'Banner creado exitosamente.')
            return redirect('autopartsBannersApp:banner_list')
    else:
        form = BannerForm()
    return render(request, 'autopartsBannersApp/banner_form.html', {
        'form': form,
        'title': 'Crear Nuevo Banner'
    })

@login_required
@user_passes_test(is_staff_or_superuser, login_url='autopartsApp:home')
def banner_edit(request, pk):
    """Edita un banner existente"""
    banner = get_object_or_404(Banner, pk=pk)
    if request.method == 'POST':
        form = BannerForm(request.POST, request.FILES, instance=banner)
        if form.is_valid():
            form.save()
            messages.success(request, 'Banner actualizado exitosamente.')
            return redirect('autopartsBannersApp:banner_list')
    else:
        form = BannerForm(instance=banner)
    return render(request, 'autopartsBannersApp/banner_form.html', {
        'form': form,
        'title': 'Editar Banner',
        'banner': banner
    })

@login_required
@user_passes_test(is_staff_or_superuser, login_url='autopartsApp:home')
def banner_delete(request, pk):
    """Elimina un banner"""
    banner = get_object_or_404(Banner, pk=pk)
    if request.method == 'POST':
        banner.delete()
        messages.success(request, 'Banner eliminado exitosamente.')
        return redirect('autopartsBannersApp:banner_list')
    return render(request, 'autopartsBannersApp/banner_confirm_delete.html', {'banner': banner})

@login_required
@user_passes_test(is_staff_or_superuser, login_url='autopartsApp:home')
def banner_toggle_active(request, pk):
    """Activa/desactiva un banner"""
    banner = get_object_or_404(Banner, pk=pk)
    banner.is_active = not banner.is_active
    banner.save()
    status = 'activado' if banner.is_active else 'desactivado'
    messages.success(request, f'Banner {status} exitosamente.')
    return redirect('autopartsBannersApp:banner_list')
