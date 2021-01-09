from django.urls import path
from django.contrib.auth import views as auth_view
from .views import register, UserProfileView, UserEditView



app_name = "account"
urlpatterns = [
    path("register/",register.as_view(), name="register"),
    path("login/", auth_view.LoginView.as_view(), name="login"),
    path("logout/", auth_view.LogoutView.as_view(), name="logout"),
    path("profile/", UserProfileView.as_view(), name="profile"),
    path("edit_profile/", UserEditView.as_view(), name="edit_profile"),
]