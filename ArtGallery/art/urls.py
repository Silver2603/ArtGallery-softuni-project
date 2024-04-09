from django.urls import path

from ArtGallery.art.views import BrowseArtsView, user_art_collection_view, AddArtPieceView, ArtPieceEditView, \
    ArtPieceDeleteView, add_comment_to_art_piece, add_like_to_art_piece

urlpatterns = [

    path("", BrowseArtsView.as_view(), name="browse_art"),
    path("profile/<str:slug>/<int:pk>/collection/", user_art_collection_view, name="art_collection"),
    path("add_art_piece/", AddArtPieceView.as_view(), name="add_art_piece"),
    path("edit_art_piece/<str:slug>/<int:pk>/", ArtPieceEditView.as_view(), name="edit_art_piece"),
    path("delete_art_piece/<str:slug>/<int:pk>/", ArtPieceDeleteView.as_view(), name="delete_art_piece"),
    path("add_comment_to_art_piece/<int:art_piece_id>/", add_comment_to_art_piece, name="add_comment_to_art_piece"),
    path("add_like_to_art_piece/<int:art_piece_id>/", add_like_to_art_piece, name="add_like_to_art_piece"),

]