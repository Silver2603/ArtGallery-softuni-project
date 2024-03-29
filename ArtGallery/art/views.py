from django.shortcuts import render
from django.views.generic import ListView

from ArtGallery.art.models import ArtPiece


class BrowseArtsView(ListView):
    model = ArtPiece
    template_name = 'art/browse.html'


