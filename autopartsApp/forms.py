from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
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


# Authentication Forms

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nombre de usuario',
        }),
        label='Nombre de usuario'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña',
        }),
        label='Contraseña'
    )


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nombre de usuario',
        }),
        label='Nombre de usuario'
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Correo electrónico',
        }),
        label='Correo electrónico'
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña',
        }),
        label='Contraseña'
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirmar contraseña',
        }),
        label='Confirmar contraseña'
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileEditForm(forms.ModelForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nombre de usuario',
        }),
        label='Nombre de usuario'
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Correo electrónico',
        }),
        label='Correo electrónico'
    )
    new_password1 = forms.CharField(
        required=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nueva contraseña (opcional)',
        }),
        label='Nueva contraseña',
        help_text='Deja en blanco si no deseas cambiar la contraseña'
    )
    new_password2 = forms.CharField(
        required=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirmar nueva contraseña',
        }),
        label='Confirmar nueva contraseña'
    )

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('new_password1')
        password2 = cleaned_data.get('new_password2')

        if password1 or password2:
            if password1 != password2:
                raise forms.ValidationError('Las contraseñas no coinciden')
        
        return cleaned_data
