from django import forms
from django.contrib.auth.forms import BaseUserCreationForm, AuthenticationForm

from ArtGallery.accounts.models import ArtGalleryUser, Profile


class ArtGalleryUserForm(BaseUserCreationForm):
    class Meta(BaseUserCreationForm.Meta):
        model = ArtGalleryUser
        fields = ("username", "email")


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ("user",)
