from django.urls import path
from autopartsApp.views import *

app_name = 'autopartsApp'

urlpatterns = [
    path("", home, name="home"),
    
    # Category URLs
    path("category/", category, name="category"),
    path("category/create/", category_create, name="category_create"),
    path("category/<int:pk>/", category_detail, name="category_detail"),
    path("category/<int:pk>/edit/", category_edit, name="category_edit"),
    path("category/<int:pk>/delete/", category_delete, name="category_delete"),
    
    # Subcategory URLs
    path("subcategory/", subcategory, name="subcategory"),
    path("subcategory/create/", subcategory_create, name="subcategory_create"),
    path("subcategory/<int:pk>/", subcategory_detail, name="subcategory_detail"),
    path("subcategory/<int:pk>/edit/", subcategory_edit, name="subcategory_edit"),
    path("subcategory/<int:pk>/delete/", subcategory_delete, name="subcategory_delete"),
    
    # Products URLs
    path("products/", products, name="products"),
    path("products/create/", products_create, name="products_create"),
    path("products/<int:pk>/", products_detail, name="products_detail"),
    path("products/<int:pk>/edit/", products_edit, name="products_edit"),
    path("products/<int:pk>/delete/", products_delete, name="products_delete"),
    
    # About Me / Contact URL
    path("about/", about_me, name="about_me"),
]