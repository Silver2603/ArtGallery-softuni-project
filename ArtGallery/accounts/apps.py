from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ArtGallery.accounts'

    def ready(self):
        import ArtGallery.accounts.signals
