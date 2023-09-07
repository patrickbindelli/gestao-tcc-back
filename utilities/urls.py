from django.urls import path
from .views import (
    UsefulFileAPIView,
    UsefulFilesAPIView,
    UsefulLinkAPIView,
    UsefulLinksAPIView,
)

# URLs para as funcionalidades relacionadas a convites e projetos de tese.
# Cada endpoint permite listar, criar, recuperar, atualizar e excluir
# convites e projetos de tese, conforme apropriado.
urlpatterns = [
    path("files/", UsefulFilesAPIView.as_view(), name="invites"),
    path("files/<int:pk>/", UsefulFileAPIView.as_view(), name="invite"),
    path("links/", UsefulLinksAPIView.as_view(), name="invites"),
    path("links/<int:pk>/", UsefulLinkAPIView.as_view(), name="invite"),
]
