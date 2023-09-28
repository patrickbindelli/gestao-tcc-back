from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    InvitesViewSet,
    ThesisProjectsViewSet,
)

from . import views

router = DefaultRouter()

router.register("invites", InvitesViewSet, basename="invites")
router.register("projects", ThesisProjectsViewSet, basename="projects")


urlpatterns = [
    path("", include(router.urls)),
]
