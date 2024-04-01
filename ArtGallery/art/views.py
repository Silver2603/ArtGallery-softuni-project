from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import ListView

from ArtGallery.accounts.models import Profile
from ArtGallery.art.models import ArtPiece

UserModel = get_user_model()


class BrowseArtsView(ListView):
    model = ArtPiece
    template_name = 'art/browse.html'


def user_art_collection_view(request, slug, pk):
    art_pieces = ArtPiece.objects.all()
    current_user = UserModel.objects.get(username=slug, pk=pk)

    context = {
        "art_pieces": art_pieces,
        "current_user": current_user,
    }

    return render(request, "art/collection.html", context)


class UserArtCollectionView(ListView):
    model = ArtPiece
    template_name = 'art/collection.html'

    def get_object(self):
        return Profile.objects.filter(pk=self.kwargs['pk'])
