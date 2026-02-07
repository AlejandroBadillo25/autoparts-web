from django.urls import path
from . import views

app_name = 'autopartsBannersApp'

urlpatterns = [
    path('', views.banner_list, name='banner_list'),
    path('crear/', views.banner_create, name='banner_create'),
    path('editar/<int:pk>/', views.banner_edit, name='banner_edit'),
    path('eliminar/<int:pk>/', views.banner_delete, name='banner_delete'),
    path('toggle/<int:pk>/', views.banner_toggle_active, name='banner_toggle_active'),
]
