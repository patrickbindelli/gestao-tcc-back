from rest_framework import generics
from .models import ThesisProject, Invite
from .serializers import ThesisProjectSerializer, InviteSerializer
from drf_spectacular.utils import extend_schema


class ThesisProjectsAPIView(generics.ListCreateAPIView):
    """
    Lista e cria projetos de tese.
    """

    queryset = ThesisProject.objects.all()
    serializer_class = ThesisProjectSerializer

    @extend_schema(
        description="Recupera uma lista de projetos de tese.",
        responses=ThesisProjectSerializer(many=True),
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        description="Cria um novo projeto de tese.",
        request=ThesisProjectSerializer,
        responses=ThesisProjectSerializer,
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class ThesisProjectAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Recupera, atualiza ou exclui um projeto de tese.
    """

    queryset = ThesisProject.objects.all()
    serializer_class = ThesisProjectSerializer

    @extend_schema(
        description="Recupera um projeto de tese pelo ID.",
        responses=ThesisProjectSerializer,
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        description="Atualiza um projeto de tese existente.",
        request=ThesisProjectSerializer,
        responses=ThesisProjectSerializer,
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        description="Atualiza parcialmente um projeto de tese existente.",
        request=ThesisProjectSerializer,
        responses=ThesisProjectSerializer,
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(
        description="Exclui um projeto de tese pelo ID.",
        responses=None,
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class InvitesAPIView(generics.ListCreateAPIView):
    """
    Lista e cria convites.
    """

    queryset = Invite.objects.all()
    serializer_class = InviteSerializer

    @extend_schema(
        description="Recupera uma lista de convites.",
        responses=InviteSerializer(many=True),
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        description="Cria um novo convite.",
        request=InviteSerializer,
        responses=InviteSerializer,
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class InviteAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Recupera, atualiza ou exclui um convite.
    """

    queryset = Invite.objects.all()
    serializer_class = InviteSerializer

    @extend_schema(
        description="Recupera uma lista de convites.",
        responses=InviteSerializer,
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        description="Atualiza um convite existente.",
        request=InviteSerializer,
        responses=InviteSerializer,
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        description="Atualiza parcialmente um convite existente.",
        request=InviteSerializer,
        responses=InviteSerializer,
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(
        description="Exclui um convite pelo ID.",
        responses=None,
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
