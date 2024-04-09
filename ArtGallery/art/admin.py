from django.contrib import admin

from ArtGallery.art.models import Likes, Comments, ArtPiece


@admin.register(ArtPiece)
class ArtPieceAdmin(admin.ModelAdmin):
    list_display = ("pk", 'title', "artist", 'user',)
    search_fields = ('user__username', 'title', 'artist',)
    ordering = ('pk',)


@admin.register(Likes)
class ArtGalleryUserLikes(admin.ModelAdmin):
    list_display = ("pk", 'to_art_piece', 'user',)
    search_fields = ('user__username', 'to_art_piece__title',)
    ordering = ('pk',)


@admin.register(Comments)
class ArtGalleryUserComments(admin.ModelAdmin):
    list_display = ("pk", "text", 'to_art_piece', 'user', "date_and_time_of_publication",)
    search_fields = ('text', "user__username", 'to_art_piece__title',)
    ordering = ('pk',)
