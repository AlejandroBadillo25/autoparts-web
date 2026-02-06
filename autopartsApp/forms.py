from django import forms
from .models import Category, Subcategory, Products


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la categoría'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción', 'rows': 3}),
            'image': forms.FileInput(attrs={
                'class': 'form-control', 
                'accept': 'image/jpeg,image/png',
                'data-placeholder': 'Formatos soportados: jpg, png'
            }),
        }
        labels = {
            'name': 'Nombre',
            'description': 'Descripción',
            'image': 'Imagen',
        }
        help_texts = {
            'image': 'Formatos soportados: jpg, png',
        }


class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = ['category', 'name', 'description', 'image']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la subcategoría'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción', 'rows': 3}),
            'image': forms.FileInput(attrs={
                'class': 'form-control', 
                'accept': 'image/jpeg,image/png',
                'data-placeholder': 'Formatos soportados: jpg, png'
            }),
        }
        labels = {
            'category': 'Categoría',
            'name': 'Nombre',
            'description': 'Descripción',
            'image': 'Imagen',
        }
        help_texts = {
            'image': 'Formatos soportados: jpg, png',
        }


class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['category', 'subcategory', 'name', 'description', 'price', 'stock', 'image']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'subcategory': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del producto'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción', 'rows': 3}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio', 'step': '0.01'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Stock'}),
            'image': forms.FileInput(attrs={
                'class': 'form-control', 
                'accept': 'image/jpeg,image/png',
                'data-placeholder': 'Formatos soportados: jpg, png'
            }),
        }
        labels = {
            'category': 'Categoría',
            'subcategory': 'Subcategoría',
            'name': 'Nombre',
            'description': 'Descripción',
            'price': 'Precio',
            'stock': 'Stock',
            'image': 'Imagen',
        }
        help_texts = {
            'image': 'Formatos soportados: jpg, png',
        }
