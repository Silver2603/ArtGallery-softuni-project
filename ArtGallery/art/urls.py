from django.urls import path

from ArtGallery.art.views import BrowseArtsView

urlpatterns = [
    path("", BrowseArtsView.as_view(), name="browse_art")
]