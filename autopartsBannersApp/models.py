from django.db import models
from django.contrib.auth.models import User
from autopartsApp.models import Category, Subcategory

# Create your models here.

class Banner(models.Model):
    SECTION_CHOICES = [
        ('inicio', 'Inicio'),
        ('categorias', 'Categorías'),
        ('subcategorias', 'Subcategorías'),
        ('productos', 'Productos'),
    ]
    
    name = models.CharField(max_length=200, verbose_name='Nombre del Banner')
    image = models.ImageField(
        upload_to='banners/',
        verbose_name='Imagen del Banner',
        help_text='Formatos permitidos: JPG, PNG'
    )
    section = models.CharField(
        max_length=20,
        choices=SECTION_CHOICES,
        verbose_name='Sección',
        help_text='Dónde se mostrará el banner'
    )
    
    # Para banners específicos de categoría o subcategoría
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='Categoría específica',
        help_text='Solo si el banner es para una categoría en particular'
    )
    subcategory = models.ForeignKey(
        Subcategory,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='Subcategoría específica',
        help_text='Solo si el banner es para una subcategoría en particular'
    )
    
    start_date = models.DateField(verbose_name='Fecha de inicio')
    end_date = models.DateField(verbose_name='Fecha de finalización')
    
    is_active = models.BooleanField(default=True, verbose_name='Activo')
    order = models.IntegerField(default=0, verbose_name='Orden de visualización')
    
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='banners_created')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'
    
    def __str__(self):
        return f"{self.name} - {self.get_section_display()}"
    
    def is_valid_date_range(self):
        """Verifica si el banner está dentro del rango de fechas válido"""
        from datetime import date
        today = date.today()
        return self.start_date <= today <= self.end_date
