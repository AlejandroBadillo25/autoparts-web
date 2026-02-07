from django.contrib import admin
from .models import Banner

# Register your models here.

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['name', 'section', 'category', 'subcategory', 'start_date', 'end_date', 'is_active', 'order', 'created_by']
    list_filter = ['section', 'is_active', 'start_date', 'end_date']
    search_fields = ['name', 'section']
    list_editable = ['is_active', 'order']
    readonly_fields = ['created_by', 'created_at', 'updated_at']
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('name', 'image', 'section')
        }),
        ('Ubicación Específica', {
            'fields': ('category', 'subcategory'),
            'description': 'Opcional: Selecciona una categoría o subcategoría específica'
        }),
        ('Periodo de Vigencia', {
            'fields': ('start_date', 'end_date')
        }),
        ('Configuración', {
            'fields': ('is_active', 'order')
        }),
        ('Información del Sistema', {
            'fields': ('created_by', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def save_model(self, request, obj, form, change):
        if not change:  # Si es un nuevo banner
            obj.created_by = request.user
        super().save_model(request, obj, form, change)
