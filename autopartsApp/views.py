from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Products, Category, Subcategory
from .forms import CategoryForm, SubcategoryForm, ProductsForm, LoginForm, RegisterForm, ProfileEditForm

# Create your views here.
def home(request):
    products_list = Products.objects.all().order_by('-created_at')
    return render(request, 'autopartsApp/index.html', {'products': products_list})

# Category Views
def category(request):
    categories = Category.objects.all().order_by('-created_at')
    busqueda = request.GET.get('busqueda', '')
    
    if busqueda:
        categories = categories.filter(name__icontains=busqueda)
    
    return render(request, 'autopartsApp/category.html', {
        'categories': categories,
        'busqueda': busqueda
    })

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('autopartsApp:category')
    else:
        form = CategoryForm()
    return render(request, 'autopartsApp/category_form.html', {'form': form, 'title': 'Crear Categoría'})

# Subcategory Views
def subcategory(request):
    subcategories = Subcategory.objects.all().order_by('-created_at')
    busqueda = request.GET.get('busqueda', '')
    
    if busqueda:
        subcategories = subcategories.filter(name__icontains=busqueda)
    
    return render(request, 'autopartsApp/subcategory.html', {
        'subcategories': subcategories,
        'busqueda': busqueda
    })

def subcategory_create(request):
    if request.method == 'POST':
        form = SubcategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('autopartsApp:subcategory')
    else:
        form = SubcategoryForm()
    return render(request, 'autopartsApp/subcategory_form.html', {'form': form, 'title': 'Crear Subcategoría'})

# Products Views
def products(request):
    products_list = Products.objects.all().order_by('-created_at')
    busqueda = request.GET.get('busqueda', '')
    
    if busqueda:
        products_list = products_list.filter(name__icontains=busqueda)
    
    return render(request, 'autopartsApp/products.html', {
        'products': products_list,
        'busqueda': busqueda
    })

def products_create(request):
    if request.method == 'POST':
        form = ProductsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('autopartsApp:products')
    else:
        form = ProductsForm()
    return render(request, 'autopartsApp/products_form.html', {'form': form, 'title': 'Crear Producto'})


# Authentication Views

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
    
    return render(request, 'autopartsApp/login.html', {'form': form})


def register_view(request):
    if request.user.is_authenticated:
        return redirect('autopartsApp:home')
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Cuenta creada exitosamente')
            return redirect('autopartsApp:login')
    else:
        form = RegisterForm()
    
    return render(request, 'autopartsApp/register.html', {'form': form})


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
            
            return redirect('autopartsApp:profile_edit')
    else:
        form = ProfileEditForm(instance=request.user)
    
    return render(request, 'autopartsApp/profile_edit.html', {'form': form})


# About Me / Contact View

def about_me(request):
    context = {
        'name': 'Alejandro Badillo Castilleja',
        'email': 'kope_alex@hotmail.com',
        'phone': '8186651164',
        'location': 'Guadalupe, Nuevo León',
        'linkedin': 'www.linkedin.com/in/alejandro-badillo25',
        'github': 'https://github.com/AlejandroBadillo25',
    }
    return render(request, 'autopartsApp/about_me.html', context)
