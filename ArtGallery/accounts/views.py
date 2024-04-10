from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from ArtGallery.accounts.forms import ArtGalleryUserForm, ProfileForm
from ArtGallery.accounts.mixins import CustomLoginRequiredMixin
from ArtGallery.accounts.models import Profile
from ArtGallery.art.models import ArtPiece, Likes

UserModel = get_user_model()


class RegisterUserView(CreateView):
    model = UserModel
    template_name = "accounts/register.html"
    form_class = ArtGalleryUserForm
    success_url = reverse_lazy("login")


class LoginUserView(LoginView):
    template_name = "accounts/login.html"
    success_url = reverse_lazy("browse_art")


class LogoutUserView(LogoutView):
    pass


class UserProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = "accounts/profile.html"

    def total_likes(self):
        all_likes = 0
        user_art_pieces = ArtPiece.objects.filter(user_id=self.object.user.id)
        for art_piece in user_art_pieces:
            for like in Likes.objects.all():
                if art_piece.id == like.to_art_piece_id:
                    all_likes += 1
        return all_likes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["art_pieces"] = ArtPiece.objects.filter(user=self.object.user)
        context["total_likes"] = self.total_likes
        return context


class UserProfileEditView(CustomLoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = "accounts/profile_edit_page.html"

    def get_success_url(self):
        return reverse_lazy("profile_details", kwargs={"slug": self.object.user.username, "pk": self.object.pk})


class UserProfileDeleteView(CustomLoginRequiredMixin, DeleteView):
    model = Profile
    template_name = "accounts/profile_delete.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        self.request.user.delete()
        return super().form_valid(form)
