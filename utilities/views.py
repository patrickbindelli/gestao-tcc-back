from rest_framework import generics
from .models import UsefulLink, UsefulFile
from .serializers import UsefulFileSerializer, UsefulLinkSerializer
from drf_spectacular.utils import extend_schema


class UsefulFilesAPIView(generics.ListCreateAPIView):
    """
    Lista e cria arquivos de utilidade.
    """

    queryset = UsefulFile.objects.all()
    serializer_class = UsefulFileSerializer

    @extend_schema(
        description="Recupera uma lista de arquivos úteis.",
        responses=UsefulFileSerializer(many=True),
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        description="Cria um novo projeto de tese.",
        request=UsefulFileSerializer,
        responses=UsefulFileSerializer,
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class UsefulFileAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Recupera, atualiza ou exclui um projeto de tese.
    """

    queryset = UsefulFile.objects.all()
    serializer_class = UsefulFileSerializer

    @extend_schema(
        description="Recupera um projeto de tese pelo ID.",
        responses=UsefulFileSerializer,
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        description="Atualiza um projeto de tese existente.",
        request=UsefulFileSerializer,
        responses=UsefulFileSerializer,
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        description="Atualiza parcialmente um projeto de tese existente.",
        request=UsefulFileSerializer,
        responses=UsefulFileSerializer,
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(
        description="Exclui um projeto de tese pelo ID.",
        responses=None,
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class UsefulLinksAPIView(generics.ListCreateAPIView):
    """
    Lista e cria arquivos de utilidade.
    """

    queryset = UsefulLink.objects.all()
    serializer_class = UsefulLinkSerializer

    @extend_schema(
        description="Recupera uma lista de arquivos úteis.",
        responses=UsefulLinkSerializer(many=True),
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        description="Cria um novo projeto de tese.",
        request=UsefulLinkSerializer,
        responses=UsefulLinkSerializer,
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class UsefulLinkAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Recupera, atualiza ou exclui um projeto de tese.
    """

    queryset = UsefulLink.objects.all()
    serializer_class = UsefulLinkSerializer

    @extend_schema(
        description="Recupera um projeto de tese pelo ID.",
        responses=UsefulLinkSerializer,
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        description="Atualiza um projeto de tese existente.",
        request=UsefulLinkSerializer,
        responses=UsefulLinkSerializer,
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        description="Atualiza parcialmente um projeto de tese existente.",
        request=UsefulLinkSerializer,
        responses=UsefulLinkSerializer,
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(
        description="Exclui um projeto de tese pelo ID.",
        responses=None,
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
