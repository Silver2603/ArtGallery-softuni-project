from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from ArtGallery.accounts.forms import ArtGalleryUserForm, ArtGalleryUserChangeForm

UserModel = get_user_model()


@admin.register(UserModel)
class ArtGalleryUserAdmin(UserAdmin):
    model = UserModel
    add_form = ArtGalleryUserForm
    form = ArtGalleryUserChangeForm

    list_display = ('pk', 'username', 'email', 'is_staff', 'is_superuser', 'date_joined')
    search_fields = ('username',)
    ordering = ('pk',)

    fieldsets = ((None, {'fields': ('username', 'password')}),
                 ('Permissions', {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')}),
                 ('Important dates', {'fields': ('last_login', "date_joined")}),)

    add_fieldsets = ((None, {"classes": ("wide",), "fields": ("username", "email", "password1", "password2"), },),)


