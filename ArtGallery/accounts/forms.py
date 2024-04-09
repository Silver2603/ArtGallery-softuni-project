from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import BaseUserCreationForm, UserChangeForm, UserCreationForm

from ArtGallery.accounts.models import ArtGalleryUser, Profile

UserModel = get_user_model()


# CHECK FOR MISS
class ArtGalleryUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ("username", "email")


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ("user",)


class ArtGalleryUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserModel

