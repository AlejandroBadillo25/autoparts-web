from django.urls import path
from .views import LoginView, RegisterView, LogoutView, ProfileEditView, ChangePasswordView

app_name = 'accountsApp'

urlpatterns = [
    # Authentication URLs
    path("login/", LoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/edit/", ProfileEditView.as_view(), name="profile_edit"),
    path("profile/change-password/", ChangePasswordView.as_view(), name="change_password"),
]
