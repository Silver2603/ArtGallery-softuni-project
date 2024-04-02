from django import forms
from django.contrib.auth.forms import BaseUserCreationForm

from ArtGallery.accounts.models import ArtGalleryUser, Profile


# CHECK FOR MISS
class ArtGalleryUserForm(BaseUserCreationForm):
    class Meta(BaseUserCreationForm.Meta):
        model = ArtGalleryUser
        fields = ("username", "email")


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ("user",)
