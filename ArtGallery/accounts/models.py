from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class ArtGalleryUser(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )

    email = models.EmailField(_("email address"), blank=False, null=False, unique=True)

    is_staff = models.BooleanField(default=False, )

    is_active = models.BooleanField(default=True, )

    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    USERNAME_FIELD = "username"

    objects = UserManager()


class Profile(models.Model):
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)

    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True, choices=[("M", "Male"), ("F", "Female")])
    favourite_artist = models.CharField(max_length=30, blank=True, null=True)

    facebook = models.CharField(max_length=30, blank=True, null=True)
    instagram = models.CharField(max_length=30, blank=True, null=True)
    profile_pic = models.URLField(blank=True, null=True)

    user = models.OneToOneField(
        ArtGalleryUser,
        on_delete=models.CASCADE,
        primary_key=True
    )
