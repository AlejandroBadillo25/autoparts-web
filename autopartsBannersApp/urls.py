from django.urls import path
from .views import (
    BannerListView, BannerCreateView, BannerUpdateView, 
    BannerDeleteView, BannerToggleActiveView
)

app_name = 'autopartsBannersApp'

urlpatterns = [
    path('', BannerListView.as_view(), name='banner_list'),
    path('crear/', BannerCreateView.as_view(), name='banner_create'),
    path('editar/<int:pk>/', BannerUpdateView.as_view(), name='banner_edit'),
    path('eliminar/<int:pk>/', BannerDeleteView.as_view(), name='banner_delete'),
    path('toggle/<int:pk>/', BannerToggleActiveView.as_view(), name='banner_toggle_active'),
]
