from django import forms
from .models import Category, Subcategory, Products


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la categoría'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción', 'rows': 3}),
        }
        labels = {
            'name': 'Nombre',
            'description': 'Descripción',
        }


class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = ['category', 'name', 'description']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la subcategoría'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción', 'rows': 3}),
        }
        labels = {
            'category': 'Categoría',
            'name': 'Nombre',
            'description': 'Descripción',
        }


class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['category', 'subcategory', 'name', 'description', 'price', 'stock']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'subcategory': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del producto'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción', 'rows': 3}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio', 'step': '0.01'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Stock'}),
        }
        labels = {
            'category': 'Categoría',
            'subcategory': 'Subcategoría',
            'name': 'Nombre',
            'description': 'Descripción',
            'price': 'Precio',
            'stock': 'Stock',
        }
