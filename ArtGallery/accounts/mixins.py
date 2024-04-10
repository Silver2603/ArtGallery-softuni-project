from django.core.exceptions import PermissionDenied


class CustomLoginRequiredMixin:
    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)

        if not self.request.user.is_authenticated or obj.user != self.request.user:
            raise PermissionDenied
        return obj
