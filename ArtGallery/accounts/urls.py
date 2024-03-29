from django.urls import path

from ArtGallery.accounts.views import RegisterUserView, LoginUserView, LogoutUserView

urlpatterns = [
    path("register/", RegisterUserView.as_view(), name="register"),
    path("login/", LoginUserView.as_view(), name="login"),
    path("logout/", LogoutUserView.as_view(), name="logout"),

]
