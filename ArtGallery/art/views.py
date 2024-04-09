from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from ArtGallery.accounts.mixins import CustomLoginRequiredMixin
from ArtGallery.accounts.models import Profile
from ArtGallery.art.forms import ArtPieceForm, CommentsForm, SearchForm
from ArtGallery.art.models import ArtPiece, Comments, Likes

UserModel = get_user_model()


class BrowseArtsView(LoginRequiredMixin, ListView):
    model = ArtPiece
    template_name = 'art/browse.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentsForm
        context['search_form'] = SearchForm(self.request.GET)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        art_piece_title = self.request.GET.get('art_piece_title')

        if art_piece_title:
            self.request.session['art_piece_title'] = art_piece_title
        else:
            self.request.session.pop('art_piece_title', None)

        art_piece_title_session = self.request.session.get('art_piece_title')

        if art_piece_title:
            queryset = queryset.filter(title__icontains=art_piece_title_session)

        return queryset


def user_art_collection_view(request, slug, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    comment_form = CommentsForm()
    art_pieces = ArtPiece.objects.filter(user_id=pk)
    search_form = SearchForm(request.GET)
    if request.method == "GET":

        art_piece_title = request.GET.get('art_piece_title')

        if art_piece_title:
            request.session['art_piece_title'] = art_piece_title
        else:
            request.session.pop('art_piece_title', None)

        art_piece_title_session = request.session.get('art_piece_title')

        if art_piece_title:
            art_pieces = art_pieces.filter(title__icontains=art_piece_title_session)

    context = {
        "art_pieces": art_pieces,
        "search_form": search_form,
        "comment_form": comment_form

    }

    return render(request, "art/collection.html", context)


class AddArtPieceView(LoginRequiredMixin, CreateView):
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


class ArtPieceEditView(CustomLoginRequiredMixin, UpdateView):
    model = ArtPiece
    form_class = ArtPieceForm
    template_name = 'art/edit_art_piece.html'

    def get_success_url(self):
        return reverse_lazy('art_collection', kwargs={'slug': self.request.user.username, "pk": self.request.user.pk})


class ArtPieceDeleteView(CustomLoginRequiredMixin, DeleteView):
    model = ArtPiece
    template_name = "art/delete_art_piece.html"

    def get_success_url(self):
        return reverse_lazy('art_collection', kwargs={'slug': self.request.user.username, "pk": self.request.user.pk})


def add_comment_to_art_piece(request, art_piece_id):
    if request.user.is_authenticated:
        art_piece = ArtPiece.objects.get(id=art_piece_id)
        form = CommentsForm(request.POST)

        if request.method == "POST":
            if form.is_valid():
                comment = form.save(commit=False)
                comment.to_art_piece = art_piece
                comment.user = request.user
                comment.save()

            return redirect(request.META['HTTP_REFERER'] + f"#{art_piece_id}")
        return redirect('home')
    else:
        return redirect('home')


def add_like_to_art_piece(request, art_piece_id):
    if request.user.is_authenticated:
        art_piece = ArtPiece.objects.get(id=art_piece_id)
        if not Likes.objects.filter(user_id=request.user.pk, to_art_piece=art_piece_id).exists():
            Likes.objects.create(user=request.user, to_art_piece=art_piece)
        else:
            like = Likes.objects.filter(user_id=request.user.pk, to_art_piece=art_piece_id)
            like.delete()
        try:
            return redirect(request.META['HTTP_REFERER'] + f"#{art_piece_id}")
        except KeyError:
            return redirect('home')
    else:
        return redirect('home')
