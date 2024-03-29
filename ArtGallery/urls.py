
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("ArtGallery.web.urls")),
    path('accounts/', include("ArtGallery.accounts.urls")),
    path('art/', include("ArtGallery.art.urls")),
]
