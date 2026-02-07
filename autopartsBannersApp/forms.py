from django import forms
from .models import Banner


class BannerForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = ['name', 'image', 'section', 'category', 'subcategory', 'start_date', 'end_date', 'is_active', 'order']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del banner'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/jpeg,image/png'
            }),
            'section': forms.Select(attrs={
                'class': 'form-control'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
            'subcategory': forms.Select(attrs={
                'class': 'form-control'
            }),
            'start_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'end_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'order': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0'
            }),
        }
        labels = {
            'name': 'Nombre del Banner',
            'image': 'Imagen',
            'section': 'Sección',
            'category': 'Categoría (opcional)',
            'subcategory': 'Subcategoría (opcional)',
            'start_date': 'Fecha de inicio',
            'end_date': 'Fecha de finalización',
            'is_active': 'Activo',
            'order': 'Orden de visualización',
        }
        help_texts = {
            'image': 'Formatos soportados: jpg, png. Tamaño recomendado: 1200x300px',
            'section': 'Selecciona dónde se mostrará el banner',
            'category': 'Solo si el banner es específico para una categoría',
            'subcategory': 'Solo si el banner es específico para una subcategoría',
            'order': 'Menor número = mayor prioridad',
        }
    
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        section = cleaned_data.get('section')
        category = cleaned_data.get('category')
        subcategory = cleaned_data.get('subcategory')
        
        # Validar que la fecha de fin sea posterior a la de inicio
        if start_date and end_date:
            if end_date < start_date:
                raise forms.ValidationError('La fecha de finalización debe ser posterior a la fecha de inicio.')
        
        # Validar coherencia entre sección y categoría/subcategoría
        if section == 'categorias' and not category:
            self.add_error('category', 'Debes seleccionar una categoría para banners de sección "Categorías".')
        
        if section == 'subcategorias' and not subcategory:
            self.add_error('subcategory', 'Debes seleccionar una subcategoría para banners de sección "Subcategorías".')
        
        return cleaned_data
