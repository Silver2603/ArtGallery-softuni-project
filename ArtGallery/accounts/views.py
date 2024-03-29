from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from ArtGallery.accounts.forms import ArtGalleryUserForm

UserModel = get_user_model()


class RegisterUserView(CreateView):
    model = UserModel
    template_name = "accounts/register.html"
    form_class = ArtGalleryUserForm
    success_url = reverse_lazy("login")


class LoginUserView(LoginView):
    template_name = "accounts/login.html"
    success_url = reverse_lazy("home")


class LogoutUserView(LogoutView):
    pass
