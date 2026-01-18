from django.urls import path
from autopartsApp.views import *

app_name = 'autopartsApp'

urlpatterns = [
    path("", home, name="home"),
    
    # Category URLs
    path("category/", category, name="category"),
    path("category/create/", category_create, name="category_create"),
    
    # Subcategory URLs
    path("subcategory/", subcategory, name="subcategory"),
    path("subcategory/create/", subcategory_create, name="subcategory_create"),
    
    # Products URLs
    path("products/", products, name="products"),
    path("products/create/", products_create, name="products_create"),
    
    # Authentication URLs
    path("login/", login_view, name="login"),
    path("register/", register_view, name="register"),
    path("logout/", logout_view, name="logout"),
    path("profile/edit/", profile_edit_view, name="profile_edit"),
    
    # About Me / Contact URL
    path("about/", about_me, name="about_me"),
]