from django.urls import path
from .views import (
    InvitesAPIView,
    InviteAPIView,
    ThesisProjectsAPIView,
    ThesisProjectAPIView,
)

# URLs para as funcionalidades relacionadas a convites e projetos de tese.
# Cada endpoint permite listar, criar, recuperar, atualizar e excluir
# convites e projetos de tese, conforme apropriado.
urlpatterns = [
    path("invites/", InvitesAPIView.as_view(), name="invites"),
    path("invites/<int:pk>/", InviteAPIView.as_view(), name="invite"),
    path("projects/", ThesisProjectsAPIView.as_view(), name="projects"),
    path("projects/<int:pk>/", ThesisProjectAPIView.as_view(), name="project"),
]
