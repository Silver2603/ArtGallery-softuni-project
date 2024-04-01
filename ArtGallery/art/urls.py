from django.urls import path

from ArtGallery.art.views import BrowseArtsView, UserArtCollectionView, user_art_collection_view

urlpatterns = [
    path("", BrowseArtsView.as_view(), name="browse_art"),
    path("profile/<str:slug>/<int:pk>/collection/", user_art_collection_view, name="art_collection"),
]