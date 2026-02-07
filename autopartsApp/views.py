from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
)
from django.urls import reverse_lazy
from datetime import date
from .models import Products, Category, Subcategory
from .forms import CategoryForm, SubcategoryForm, ProductsForm


# Home View
class HomeView(ListView):
    model = Products
    template_name = 'autopartsApp/index.html'
    context_object_name = 'products'
    ordering = ['-created_at']


# ==================== CATEGORY VIEWS ====================

class CategoryListView(ListView):
    model = Category
    template_name = 'autopartsApp/category.html'
    context_object_name = 'categories'
    ordering = ['-created_at']
    
    def get_queryset(self):
        queryset = super().get_queryset()
        busqueda = self.request.GET.get('busqueda', '')
        if busqueda:
            queryset = queryset.filter(name__icontains=busqueda)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['busqueda'] = self.request.GET.get('busqueda', '')
        return context


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'autopartsApp/category_detail.html'
    context_object_name = 'category'


class CategoryCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'autopartsApp/category_form.html'
    success_url = reverse_lazy('autopartsApp:category')
    permission_required = 'autopartsApp.add_category'
    login_url = 'autopartsApp:home'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Categoría'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'Categoría creada exitosamente.')
        return super().form_valid(form)


class CategoryUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'autopartsApp/category_form.html'
    success_url = reverse_lazy('autopartsApp:category')
    permission_required = 'autopartsApp.change_category'
    login_url = 'autopartsApp:home'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Categoría'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'Categoría actualizada exitosamente.')
        return super().form_valid(form)


class CategoryDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Category
    template_name = 'autopartsApp/category_confirm_delete.html'
    context_object_name = 'category'
    success_url = reverse_lazy('autopartsApp:category')
    permission_required = 'autopartsApp.delete_category'
    login_url = 'autopartsApp:home'
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Categoría eliminada exitosamente.')
        return super().delete(request, *args, **kwargs)


# ==================== SUBCATEGORY VIEWS ====================

class SubcategoryListView(ListView):
    model = Subcategory
    template_name = 'autopartsApp/subcategory.html'
    context_object_name = 'subcategories'
    ordering = ['-created_at']
    
    def get_queryset(self):
        queryset = super().get_queryset()
        busqueda = self.request.GET.get('busqueda', '')
        if busqueda:
            queryset = queryset.filter(name__icontains=busqueda)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['busqueda'] = self.request.GET.get('busqueda', '')
        return context


class SubcategoryDetailView(DetailView):
    model = Subcategory
    template_name = 'autopartsApp/subcategory_detail.html'
    context_object_name = 'subcategory'
    
    def get_context_data(self, **kwargs):
        from autopartsBannersApp.models import Banner
        context = super().get_context_data(**kwargs)
        today = date.today()
        
        # Obtener banners específicos de esta subcategoría
        subcategory_banners = Banner.objects.filter(
            is_active=True,
            start_date__lte=today,
            end_date__gte=today,
            subcategory=self.object
        )
        context['subcategory_specific_banners'] = subcategory_banners
        return context


class SubcategoryCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Subcategory
    form_class = SubcategoryForm
    template_name = 'autopartsApp/subcategory_form.html'
    success_url = reverse_lazy('autopartsApp:subcategory')
    permission_required = 'autopartsApp.add_subcategory'
    login_url = 'autopartsApp:home'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Subcategoría'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'Subcategoría creada exitosamente.')
        return super().form_valid(form)


class SubcategoryUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Subcategory
    form_class = SubcategoryForm
    template_name = 'autopartsApp/subcategory_form.html'
    success_url = reverse_lazy('autopartsApp:subcategory')
    permission_required = 'autopartsApp.change_subcategory'
    login_url = 'autopartsApp:home'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Subcategoría'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'Subcategoría actualizada exitosamente.')
        return super().form_valid(form)


class SubcategoryDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Subcategory
    template_name = 'autopartsApp/subcategory_confirm_delete.html'
    context_object_name = 'subcategory'
    success_url = reverse_lazy('autopartsApp:subcategory')
    permission_required = 'autopartsApp.delete_subcategory'
    login_url = 'autopartsApp:home'
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Subcategoría eliminada exitosamente.')
        return super().delete(request, *args, **kwargs)


# ==================== PRODUCTS VIEWS ====================

class ProductsListView(ListView):
    model = Products
    template_name = 'autopartsApp/products.html'
    context_object_name = 'products'
    ordering = ['-created_at']
    
    def get_queryset(self):
        queryset = super().get_queryset()
        busqueda = self.request.GET.get('busqueda', '')
        if busqueda:
            queryset = queryset.filter(name__icontains=busqueda)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['busqueda'] = self.request.GET.get('busqueda', '')
        return context


class ProductsDetailView(DetailView):
    model = Products
    template_name = 'autopartsApp/products_detail.html'
    context_object_name = 'product'


class ProductsCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Products
    form_class = ProductsForm
    template_name = 'autopartsApp/products_form.html'
    success_url = reverse_lazy('autopartsApp:products')
    permission_required = 'autopartsApp.add_products'
    login_url = 'autopartsApp:home'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Producto'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'Producto creado exitosamente.')
        return super().form_valid(form)


class ProductsUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Products
    form_class = ProductsForm
    template_name = 'autopartsApp/products_form.html'
    success_url = reverse_lazy('autopartsApp:products')
    permission_required = 'autopartsApp.change_products'
    login_url = 'autopartsApp:home'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Producto'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'Producto actualizado exitosamente.')
        return super().form_valid(form)


class ProductsDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Products
    template_name = 'autopartsApp/products_confirm_delete.html'
    context_object_name = 'product'
    success_url = reverse_lazy('autopartsApp:products')
    permission_required = 'autopartsApp.delete_products'
    login_url = 'autopartsApp:home'
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Producto eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)


# ==================== ABOUT ME VIEW ====================

class AboutMeView(TemplateView):
    template_name = 'autopartsApp/about_me.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Obtener perfil del usuario "Dumas" para mostrar siempre su foto
        from django.contrib.auth.models import User
        from accountsApp.models import UserProfile
        profile = None
        try:
            dumas_user = User.objects.get(username='Dumas')
            profile, created = UserProfile.objects.get_or_create(user=dumas_user)
        except User.DoesNotExist:
            pass
        
        context.update({
            'name': 'Alejandro Badillo Castilleja',
            'email': 'kope_alex@hotmail.com',
            'phone': '8186651164',
            'location': 'Guadalupe, Nuevo León',
            'linkedin': 'www.linkedin.com/in/alejandro-badillo25',
            'github': 'https://github.com/AlejandroBadillo25',
            'profile': profile,
        })
        return context
