from django.shortcuts import render, redirect
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