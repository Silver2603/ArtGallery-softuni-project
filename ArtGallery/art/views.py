from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from ArtGallery.accounts.models import Profile
from ArtGallery.art.models import ArtPiece

UserModel = get_user_model()


class BrowseArtsView(ListView):
    model = ArtPiece
    template_name = 'art/browse.html'


def user_art_collection_view(request, slug, pk):
    art_pieces = ArtPiece.objects.filter(user_id=pk)

    context = {
        "art_pieces": art_pieces,
    }

    return render(request, "art/collection.html", context)


class AddArtPieceView(CreateView):
    model = ArtPiece
    fields = ("title", "art_piece", "artist", "type_of_artwork", "price", "description",)
    template_name = 'art/add_art_piece.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('art_collection', kwargs={'slug': self.request.user.username, "pk": self.request.user.pk})
