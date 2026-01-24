from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Products, Category, Subcategory
from .forms import CategoryForm, SubcategoryForm, ProductsForm

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

@login_required
def category_detail(request, pk):
    category_obj = get_object_or_404(Category, pk=pk)
    return render(request, 'autopartsApp/category_detail.html', {'category': category_obj})

@login_required
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría creada exitosamente.')
            return redirect('autopartsApp:category')
    else:
        form = CategoryForm()
    return render(request, 'autopartsApp/category_form.html', {'form': form, 'title': 'Crear Categoría'})

@login_required
def category_edit(request, pk):
    category_obj = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category_obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría actualizada exitosamente.')
            return redirect('autopartsApp:category')
    else:
        form = CategoryForm(instance=category_obj)
    return render(request, 'autopartsApp/category_form.html', {'form': form, 'title': 'Editar Categoría'})

@login_required
def category_delete(request, pk):
    category_obj = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category_obj.delete()
        messages.success(request, 'Categoría eliminada exitosamente.')
        return redirect('autopartsApp:category')
    return render(request, 'autopartsApp/category_confirm_delete.html', {'category': category_obj})

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

@login_required
def subcategory_detail(request, pk):
    subcategory_obj = get_object_or_404(Subcategory, pk=pk)
    return render(request, 'autopartsApp/subcategory_detail.html', {'subcategory': subcategory_obj})

@login_required
def subcategory_create(request):
    if request.method == 'POST':
        form = SubcategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subcategoría creada exitosamente.')
            return redirect('autopartsApp:subcategory')
    else:
        form = SubcategoryForm()
    return render(request, 'autopartsApp/subcategory_form.html', {'form': form, 'title': 'Crear Subcategoría'})

@login_required
def subcategory_edit(request, pk):
    subcategory_obj = get_object_or_404(Subcategory, pk=pk)
    if request.method == 'POST':
        form = SubcategoryForm(request.POST, instance=subcategory_obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subcategoría actualizada exitosamente.')
            return redirect('autopartsApp:subcategory')
    else:
        form = SubcategoryForm(instance=subcategory_obj)
    return render(request, 'autopartsApp/subcategory_form.html', {'form': form, 'title': 'Editar Subcategoría'})

@login_required
def subcategory_delete(request, pk):
    subcategory_obj = get_object_or_404(Subcategory, pk=pk)
    if request.method == 'POST':
        subcategory_obj.delete()
        messages.success(request, 'Subcategoría eliminada exitosamente.')
        return redirect('autopartsApp:subcategory')
    return render(request, 'autopartsApp/subcategory_confirm_delete.html', {'subcategory': subcategory_obj})

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

@login_required
def products_detail(request, pk):
    product = get_object_or_404(Products, pk=pk)
    return render(request, 'autopartsApp/products_detail.html', {'product': product})

@login_required
def products_create(request):
    if request.method == 'POST':
        form = ProductsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto creado exitosamente.')
            return redirect('autopartsApp:products')
    else:
        form = ProductsForm()
    return render(request, 'autopartsApp/products_form.html', {'form': form, 'title': 'Crear Producto'})

@login_required
def products_edit(request, pk):
    product = get_object_or_404(Products, pk=pk)
    if request.method == 'POST':
        form = ProductsForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado exitosamente.')
            return redirect('autopartsApp:products')
    else:
        form = ProductsForm(instance=product)
    return render(request, 'autopartsApp/products_form.html', {'form': form, 'title': 'Editar Producto'})

@login_required
def products_delete(request, pk):
    product = get_object_or_404(Products, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Producto eliminado exitosamente.')
        return redirect('autopartsApp:products')
    return render(request, 'autopartsApp/products_confirm_delete.html', {'product': product})


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
