from django import forms

from ArtGallery.art.models import ArtPiece, Comments


class ArtPieceForm(forms.ModelForm):
    class Meta:
        model = ArtPiece
        fields = ("title", "art_piece", "artist", "type_of_artwork", "price", "description",)


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['text']
        widgets = {
            'comment_text': forms.Textarea(attrs={'placeholder': 'Add comment...'}),

        }


class SearchForm(forms.Form):
    art_piece_title = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Search Art Piece...'}),
        required=False,
    )
