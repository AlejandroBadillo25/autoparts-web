from django.urls import path
from accountsApp.views import *

app_name = 'accountsApp'

urlpatterns = [
    # Authentication URLs
    path("login/", login_view, name="login"),
    path("register/", register_view, name="register"),
    path("logout/", logout_view, name="logout"),
    path("profile/edit/", profile_edit_view, name="profile_edit"),
    path("profile/change-password/", change_password_view, name="change_password"),
]
