from django.urls import path

from ArtGallery.accounts.views import RegisterUserView, LoginUserView, LogoutUserView, UserProfileView, \
    UserProfileEditView, UserProfileDeleteView

urlpatterns = [
    path("register/", RegisterUserView.as_view(), name="register"),
    path("login/", LoginUserView.as_view(), name="login"),
    path("logout/", LogoutUserView.as_view(), name="logout"),
    path("profile/<str:slug>/<int:pk>/", UserProfileView.as_view(), name="profile_details"),
    path("profile/<str:slug>/<int:pk>/edit/", UserProfileEditView.as_view(), name="profile_edit"),
    path("profile/<str:slug>/<int:pk>/delete/", UserProfileDeleteView.as_view(), name="profile_delete"),


]
