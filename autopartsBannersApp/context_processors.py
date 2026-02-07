from datetime import date
from .models import Banner


def banners_context(request):
    """
    Context processor para hacer los banners disponibles en todos los templates
    """
    today = date.today()
    
    # Obtener banners activos y dentro del rango de fechas
    active_banners = Banner.objects.filter(
        is_active=True,
        start_date__lte=today,
        end_date__gte=today
    )
    
    # Organizar banners por sección
    return {
        'banners_inicio': active_banners.filter(section='inicio'),
        'banners_categorias': active_banners.filter(section='categorias'),
        'banners_subcategorias': active_banners.filter(section='subcategorias'),
        'banners_productos': active_banners.filter(section='productos'),
    }
