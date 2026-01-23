from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm, RegisterForm, ProfileEditForm


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
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
            
            # Cambiar contraseña si se proporcionó una nueva
            new_password = form.cleaned_data.get('new_password1')
            if new_password:
                user.set_password(new_password)
                user.save()
                update_session_auth_hash(request, user)  # Mantener la sesión activa
                messages.success(request, 'Perfil y contraseña actualizados exitosamente.')
            else:
                messages.success(request, 'Perfil actualizado exitosamente.')
            
            return redirect('accountsApp:profile_edit')
    else:
        form = ProfileEditForm(instance=request.user)
    
    return render(request, 'accountsApp/profile_edit.html', {'form': form})
