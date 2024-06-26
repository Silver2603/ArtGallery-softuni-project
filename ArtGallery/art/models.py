from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class ArtPiece(models.Model):
    TYPES_OF_ARTWORK = (
        ("Picture", "Picture"),
        ("Drawing", "Drawing"),
        ("Sculpture", "Sculpture"),
        ("Other", "Other")
    )

    title = models.CharField(max_length=30, null=False, blank=False, unique=True)

    art_piece = models.URLField(null=False, blank=False, unique=True)

    artist = models.CharField(max_length=30, null=True, blank=True)

    type_of_artwork = models.CharField(max_length=30, choices=TYPES_OF_ARTWORK, null=True, blank=True)

    description = models.TextField(null=True, blank=True)

    price = models.FloatField(null=True, blank=True)

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)


class Comments(models.Model):
    text = models.CharField(null=True, blank=True,max_length=200)
    date_and_time_of_publication = models.DateTimeField(auto_now_add=True)
    to_art_piece = models.ForeignKey(ArtPiece, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)


class Likes(models.Model):
    to_art_piece = models.ForeignKey(ArtPiece, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
