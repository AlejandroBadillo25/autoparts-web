from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .forms import LoginForm, RegisterForm, ProfileEditForm, ChangePasswordForm
from .models import UserProfile


def login_view(request):
    if request.user.is_authenticated:
        return redirect('autopartsApp:home')
    
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'¡Bienvenido {username}!')
                return redirect('autopartsApp:home')
    else:
        form = LoginForm()
    
    return render(request, 'accountsApp/login.html', {'form': form})


def register_view(request):
    if request.user.is_authenticated:
        return redirect('autopartsApp:home')
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Crear perfil de usuario automáticamente
            UserProfile.objects.create(user=user)
            messages.success(request, f'Cuenta creada exitosamente')
            return redirect('accountsApp:login')
    else:
        form = RegisterForm()
    
    return render(request, 'accountsApp/register.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, 'Has cerrado sesión exitosamente.')
    return redirect('autopartsApp:home')


@login_required
def profile_edit_view(request):
    # Crear perfil si no existe
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            user = form.save()
            
            # Actualizar o crear perfil con phone, address y profile_image
            profile.phone = form.cleaned_data.get('phone')
            profile.address = form.cleaned_data.get('address')
            
            # Guardar imagen de perfil si fue proporcionada
            if 'profile_image' in request.FILES:
                profile.profile_image = request.FILES['profile_image']
            
            profile.save()
            
            messages.success(request, 'Perfil actualizado exitosamente.')
            return redirect('accountsApp:profile_edit')
    else:
        form = ProfileEditForm(instance=request.user)
    
    return render(request, 'accountsApp/profile_edit.html', {'form': form, 'profile': profile})


@login_required
def change_password_view(request):
    if request.method == 'POST':
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
