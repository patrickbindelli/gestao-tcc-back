from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
)

urlpatterns = [
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("research/", include("research.urls"), name="research"),
    path("utilities/", include("utilities.urls"), name="utilities"),
    path(
        "docs",
        SpectacularRedocView.as_view(),
        name="docs",
    ),
    path("docs/schema/", SpectacularAPIView.as_view(), name="schema"),
]
