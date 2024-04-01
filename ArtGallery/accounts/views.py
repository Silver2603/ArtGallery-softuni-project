from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from ArtGallery.accounts.forms import ArtGalleryUserForm, ProfileForm
from ArtGallery.accounts.models import Profile
from ArtGallery.art.models import ArtPiece

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


class UserProfileView(DetailView):
    model = Profile
    template_name = "accounts/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["artpieces"] = ArtPiece.objects.filter(user=self.request.user)
        return context


class UserProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = "accounts/profile_edit_page.html"

    def get_success_url(self):
        return reverse_lazy("profile_details", kwargs={"slug": self.object.user.username, "pk": self.object.pk})


class UserProfileDeleteView(DeleteView):
    model = Profile
    template_name = "accounts/profile_delete.html"
    success_url = reverse_lazy("home")

    def get_object(self, queryset=None):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return redirect(self.get_success_url())
