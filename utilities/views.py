from .models import UsefulLink, UsefulFile
from .serializers import UsefulFileSerializer, UsefulLinkSerializer
from rest_framework import viewsets


class UsefulFilesViewSet(viewsets.ModelViewSet):
    """
    Lista e cria arquivos de utilidade.
    """

    queryset = UsefulFile.objects.all()
    serializer_class = UsefulFileSerializer


class UsefulLinksViewSet(viewsets.ModelViewSet):
    """
    Lista e cria arquivos de utilidade.
    """

    queryset = UsefulLink.objects.all()
    serializer_class = UsefulLinkSerializer
