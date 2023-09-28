from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UsefulFilesViewSet,
    UsefulLinksViewSet,
)


router = DefaultRouter()

router.register("files", UsefulFilesViewSet, basename="files")
router.register("links", UsefulLinksViewSet, basename="links")


urlpatterns = [
    path("", include(router.urls)),
]
