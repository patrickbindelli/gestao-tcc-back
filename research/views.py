from .models import ThesisProject, Invite
from .serializers import ThesisProjectSerializer, InviteSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets


class ThesisProjectsViewSet(viewsets.ModelViewSet):
    """
    Lista e cria projetos de tese.
    """

    queryset = ThesisProject.objects.all()
    serializer_class = ThesisProjectSerializer

    @action(detail=False, methods=["get"])
    def ongoing(self, request):
        user = request.user
        queryset = self.get_queryset().filter(approved=False, authors=user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def approved(self, request):
        user = request.user
        queryset = self.get_queryset().filter(approved=True, authors=user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class InvitesViewSet(viewsets.ModelViewSet):
    """
    Lista e cria convites.
    """

    queryset = Invite.objects.all()
    serializer_class = InviteSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = super().get_queryset()
        queryset = queryset.filter(receiver=user)
        return queryset
