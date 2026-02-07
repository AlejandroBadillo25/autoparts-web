from django.urls import path
from .views import (
    HomeView,
    CategoryListView, CategoryDetailView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView,
    SubcategoryListView, SubcategoryDetailView, SubcategoryCreateView, SubcategoryUpdateView, SubcategoryDeleteView,
    ProductsListView, ProductsDetailView, ProductsCreateView, ProductsUpdateView, ProductsDeleteView,
    AboutMeView
)

app_name = 'autopartsApp'

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    
    # Category URLs
    path("category/", CategoryListView.as_view(), name="category"),
    path("category/create/", CategoryCreateView.as_view(), name="category_create"),
    path("category/<int:pk>/", CategoryDetailView.as_view(), name="category_detail"),
    path("category/<int:pk>/edit/", CategoryUpdateView.as_view(), name="category_edit"),
    path("category/<int:pk>/delete/", CategoryDeleteView.as_view(), name="category_delete"),
    
    # Subcategory URLs
    path("subcategory/", SubcategoryListView.as_view(), name="subcategory"),
    path("subcategory/create/", SubcategoryCreateView.as_view(), name="subcategory_create"),
    path("subcategory/<int:pk>/", SubcategoryDetailView.as_view(), name="subcategory_detail"),
    path("subcategory/<int:pk>/edit/", SubcategoryUpdateView.as_view(), name="subcategory_edit"),
    path("subcategory/<int:pk>/delete/", SubcategoryDeleteView.as_view(), name="subcategory_delete"),
    
    # Products URLs
    path("products/", ProductsListView.as_view(), name="products"),
    path("products/create/", ProductsCreateView.as_view(), name="products_create"),
    path("products/<int:pk>/", ProductsDetailView.as_view(), name="products_detail"),
    path("products/<int:pk>/edit/", ProductsUpdateView.as_view(), name="products_edit"),
    path("products/<int:pk>/delete/", ProductsDeleteView.as_view(), name="products_delete"),
    
    # About Me / Contact URL
    path("about/", AboutMeView.as_view(), name="about_me"),
]