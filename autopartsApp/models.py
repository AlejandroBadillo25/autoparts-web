from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(
        upload_to='category_images/',
        blank=True,
        null=True,
        verbose_name='Imagen de Categoría',
        help_text='Formatos permitidos: JPG, PNG'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.created_at}"

class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(
        upload_to='subcategory_images/',
        blank=True,
        null=True,
        verbose_name='Imagen de Subcategoría',
        help_text='Formatos permitidos: JPG, PNG'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.created_at}"

class Products(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image = models.ImageField(
        upload_to='product_images/',
        blank=True,
        null=True,
        verbose_name='Imagen de Producto',
        help_text='Formatos permitidos: JPG, PNG'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.price}"