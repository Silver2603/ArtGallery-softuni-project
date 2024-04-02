from django.urls import path

from ArtGallery.art.views import BrowseArtsView, user_art_collection_view, AddArtPieceView

urlpatterns = [
    path("", BrowseArtsView.as_view(), name="browse_art"),
    path("profile/<str:slug>/<int:pk>/collection/", user_art_collection_view, name="art_collection"),
    path("add_art_piece/", AddArtPieceView.as_view(), name="add_art_piece"),

]